from qChronolyze import filtDown, getSorter

def qChronoMd(dicti,flnm,tafs):
    mdFile = f'data/compare/{flnm}.md'
    instLstAgg = []
    queriesLeft = { f'{k} ({v})' for k,v in dicti.items() }
    alreadyRefed = []
    for rt in dicti.keys():
        instLst = filtDown(rt,dicti[rt])
        instLstAgg += instLst
    # instLstAgg = [ { 
    #     **row, 
    #     "ayah_link": f"<a style='color:rgb(50,50,200)' href='https://quran.com/{row['surah:ayah']}/tafsirs/{tafs}'>{row['ayah_link']}</a>"
    #     } for row in instLstAgg ]
    import pandas as pd

    df = pd.DataFrame(instLstAgg)
    sorter = getSorter()
    df['surah:ayah'] = pd.Categorical(df['surah:ayah'], categories=sorter, ordered=True)
    df.sort_values(["surah:ayah","position"],inplace=True)
    # df.reset_index(drop=True,inplace=True)
    sortedRecs = df.to_dict(orient='records')

    for rec in sortedRecs:
        if rec["surah:ayah"] not in alreadyRefed:
            with open(mdFile, 'a') as f:
                f.write(
                    f'\n# Q:{rec["surah:ayah"]}\n'
                    + f'\n[Q.{rec["surah:ayah"]}](https://quran.com/{rec["surah:ayah"]}/tafsirs/{tafs})\n'
                    + f'\n![[QsortedRukued#{rec["surah:ayah"]}]]\n'
                )
            alreadyRefed.append(rec["surah:ayah"])
        if rec["query"] in queriesLeft:
            with open(mdFile, 'a') as f:
                f.write(f'\n## {rec["query"]}\n')
                queriesLeft.remove(rec["query"])
        

