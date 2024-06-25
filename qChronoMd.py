# from qChronolyze import filtDown, getSorter
from qChronolyze import aggregLsts, getSorter

def qChronoMd(dicti,flnm,tafs):
    mdFile = f'data/compare/{flnm}.md'
    # instLstAgg = []
    
    alreadyRefed = []
    instLstAgg = aggregLsts(dicti,tafs)

    import pandas as pd

    df = pd.DataFrame(instLstAgg)
    sorter = getSorter()
    df['surah:ayah'] = pd.Categorical(df['surah:ayah'], categories=sorter, ordered=True)
    df.sort_values(["surah:ayah","position"],inplace=True)
    # df.reset_index(drop=True,inplace=True)
    sortedRecs = df.to_dict(orient='records')


    newDic = {}

    for rec in sortedRecs:
        if rec["surah:ayah"] not in newDic.keys():
            newDic[rec["surah:ayah"]] = {
                'string': f'\n[Q.{rec["surah:ayah"]}](https://quran.com/{rec["surah:ayah"]}/tafsirs/{tafs})\n'
                            + f'\n![[Qrsed#{rec["surah:ayah"]}]]\n',
                # 'queries': [
                #     {
                #         'query': rec["query"],
                #         'postquery': ''
                #     }
                # ]
                'queries': {
                    rec["query"]: '\n\n'
                }
            }
        else:
            # newDic[rec["surah:ayah"]]["queries"].append(
            #     {
            #         'query': rec["query"], 
            #         'postquery': '',
            #     }
            # )
            newDic[rec["surah:ayah"]]["queries"][rec["query"]] = '\n\n'



    # print('\nnewDic before checking md: ', newDic, '\n')

    import os

    if os.path.isfile(mdFile):
        import re

        with open(mdFile) as f:
            strn = f.read()

        olds = re.compile(
                '\n#\s*(?:Q\:){0,1}(\d{1,}\:\d{1,})(.*?(?=\n#|$))(?:(\n##\s{1,}.*?(?=\n#\s{1,}|$))){0,1}',
                re.DOTALL
            ).findall(

            strn
        )


        # print(len(rep))

        oldSurAyLs = [x[0] for x in olds]

        # print(f'\nold surAy list: {oldSurAyLs}\n\nnew surAy list: {newDic.keys()}\n')

        j = 0
        for nk in newDic.keys():
            if nk not in oldSurAyLs:
                j+=1
                print(f'new not in old {j}: {nk}')
        
        i = 0

        for old in olds:

            if old[0] not in newDic.keys():
                newDic[old[0]] = { 
                    'string' : old[1] , 
                    'queries': {
                        quer[0]: quer[1]
                        
                        
                        # quer
                        for quer in re.compile(
                            '\n##\s{1,}([^\n]{1,}(?=\n))(.*?(?=\n#|$))',    
                            re.DOTALL,
                        ).findall(
                            old[2] 
                        )
                    }
                        if len(old) > 2 else {}
                    # 'queries': [
                    #     {
                    #         'query': quer[0],
                    #         'postquery': quer[1],
                        
                    #     }
                    #     # quer
                    #     for quer in re.compile(
                    #         '\n##\s{1,}([^\n]{1,}(?=\n))(.*?(?=\n))',    
                    #         re.DOTALL,
                    #     ).findall(
                    #         old[2] 
                    #     )
                    # ]
                    #     if len(old) > 2 else None 
                }

                i+=1
                print(f'\nold not in new {i}: {old[0]}')

            else:
                newDic[old[0]]['string'] = old[1]
                bef = dict(newDic[old[0]])
                for quer in re.compile(
                            '\n##\s{1,}([^\n]{1,}(?=\n))(.*?(?=\n#|$))',    
                            re.DOTALL,
                        ).findall(
                            old[2] 
                        ):
                    newDic[old[0]]['queries'][quer[0]] = quer[1]
                    # newDic[old[0]]['queries'].append({
                    #         'query': quer[0],
                    #         'postquery': quer[1],
                        
                    #     })
                if bef != newDic[old[0]]:
                    print(f'\nVerse string before reading: {bef}')
                    print(f'\nVerse string after reading: {newDic[old[0]]}')
        

    # print('\nnewDic after checking md: ', newDic, '\n')
    # print(newDic)

    sorterIdxs = [sorter.index(suray) for suray in newDic.keys()]

    sorterIdxs.sort()

    surAyOrdered = [sorter[idx] for idx in sorterIdxs]

    
    newStr = ''

    print(f"\nNumber of ayahs: {len(surAyOrdered)}")

    queriesLeft = set()
    for surAy in surAyOrdered:
        for q in newDic[surAy]['queries'].keys():
            queriesLeft.add(q)

    for surAy in surAyOrdered:
        if surAy == '68:2':
            print(f'\nnew string: {newDic[surAy]}\n')
        # newStrUp =   f'\n# Q:{surAy}\n' + f'\n[Q.{surAy}](https://quran.com/{surAy}/tafsirs/{tafs})\n' + f'\n![[Qrsed#{surAy}]]\n'
        # qpq = newDic[surAy]['queries'].items()
        newStrUp =   f'\n\n# Q:{surAy}' + newDic[surAy]['string']

        newStr += newStrUp

        # alreadyRefed.append(rec["surah:ayah"])
        alreadyRefed.append(surAy)
        # for query in newDic[surAy]['queries']:
        #     if query['query'] in queriesLeft:
        #         print(f'\nquery left at {surAy} : {query["query"]}')
        #         newStrUp = f'\n## {query["query"]}\n' + query['postquery']
        #         newStr += newStrUp
        #         queriesLeft.remove(query["query"])

        

        for q, pq in newDic[surAy]['queries'].items():
            if q in queriesLeft:
                print(f'\nquery left at {surAy} : {q}')
                newStrUp = f'\n## {q}' + pq
                newStr += newStrUp
                queriesLeft.remove(q)
                

    with open(mdFile, 'w+') as f:
        f.write(newStr)
        

