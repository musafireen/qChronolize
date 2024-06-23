# from qChronolyze import filtDown, getSorter
from qChronolyze import aggregLsts, getSorter

def qChronoMd(dicti,flnm,tafs):
    mdFile = f'data/compare/{flnm}.md'
    # instLstAgg = []
    queriesLeft = { f'{list(item.keys())[0]} ({list(item.values())[0]})' for item in dicti }
    alreadyRefed = []
    instLstAgg = aggregLsts(dicti,tafs)

    import pandas as pd

    df = pd.DataFrame(instLstAgg)
    sorter = getSorter()
    df['surah:ayah'] = pd.Categorical(df['surah:ayah'], categories=sorter, ordered=True)
    df.sort_values(["surah:ayah","position"],inplace=True)
    # df.reset_index(drop=True,inplace=True)
    sortedRecs = df.to_dict(orient='records')


    repDic = {}

    for rec in sortedRecs:
        if rec["surah:ayah"] not in repDic.keys():
            repDic[rec["surah:ayah"]] = {
                'string': f'\n[Q.{rec["surah:ayah"]}](https://quran.com/{rec["surah:ayah"]}/tafsirs/{tafs})\n'
                            + f'\n![[Qrsed#{rec["surah:ayah"]}]]\n',
                # 'queries': [
                #     {
                #         'query': rec["query"],
                #         'postquery': ''
                #     }
                # ]
                'queries': {
                    rec["query"]: ''
                }
            }
        else:
            # repDic[rec["surah:ayah"]]["queries"].append(
            #     {
            #         'query': rec["query"], 
            #         'postquery': '',
            #     }
            # )
            repDic[rec["surah:ayah"]]["queries"][rec["query"]] = ''



    # print('\nrepDic before checking md: ', repDic, '\n')

    import os

    if os.path.isfile(mdFile):
        import re

        with open(mdFile) as f:
            strn = f.read()

        rep = re.compile(
                '\n#\s*(?:Q\:){0,1}(\d{1,}\:\d{1,})(.*?(?=\n#|$))(?:(\n##\s{1,}.*?(?=\n#\s{1,}|$))){0,1}',
                re.DOTALL
            ).findall(

            strn
        )


        # print(len(rep))

        for setty in rep:
            if setty[0] not in repDic:
                repDic[setty[0]] = { 
                    'string' : setty[1] , 
                    'queries': {
                        quer[0]: quer[1]
                        
                        
                        # quer
                        for quer in re.compile(
                            '\n##\s{1,}([^\n]{1,}(?=\n))(.*?(?=\n))',    
                            re.DOTALL,
                        ).findall(
                            setty[2] 
                        )
                    }
                        if len(setty) > 2 else {}
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
                    #         setty[2] 
                    #     )
                    # ]
                    #     if len(setty) > 2 else None 
                }
            else:
                print(f'\nVerse string before: {repDic[setty[0]]}')
                for quer in re.compile(
                            '\n##\s{1,}([^\n]{1,}(?=\n))(.*?(?=\n))',    
                            re.DOTALL,
                        ).findall(
                            setty[2] 
                        ):
                    repDic[setty[0]]['string'] = setty[1]
                    repDic[setty[0]]['queries'][quer[0]] = quer[1]
                    # repDic[setty[0]]['queries'].append({
                    #         'query': quer[0],
                    #         'postquery': quer[1],
                        
                    #     })
                    
                print(f'\nVerse string after: {repDic[setty[0]]}')
        

    # print('\nrepDic after checking md: ', repDic, '\n')
    # print(repDic)

    sorterIdxs = [sorter.index(suray) for suray in repDic.keys()]

    surAyOrdered = [sorter[idx] for idx in sorterIdxs]
    
    newStr = ''

    for surAy in surAyOrdered:       
        newStrUp =   f'\n# Q:{surAy}\n' + f'\n[Q.{surAy}](https://quran.com/{surAy}/tafsirs/{tafs})\n' + f'\n![[Qrsed#{surAy}]]\n'

        newStr += newStrUp

        alreadyRefed.append(rec["surah:ayah"])
        # for query in repDic[surAy]['queries']:
        #     if query['query'] in queriesLeft:
        #         print(f'\nquery left at {surAy} : {query["query"]}')
        #         newStrUp = f'\n## {query["query"]}\n' + query['postquery']
        #         newStr += newStrUp
        #         queriesLeft.remove(query["query"])
        for q, pq in repDic[surAy]['queries'].items():
            if q in queriesLeft:
                print(f'\nquery left at {surAy} : {q}')
                newStrUp = f'\n## {q}\n' + pq
                newStr += newStrUp
                queriesLeft.remove(q)

    with open(mdFile, 'w+') as f:
        f.write(newStr)
        

