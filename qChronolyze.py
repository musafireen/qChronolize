def confPres(pres):
    '''Sets configuration'''
    presDict={'1':'table','2':'plot'}
    if pres not in presDict.values():
      if pres in presDict.keys():
        pres=presDict[pres]
      else:
        if pres=='' or pres=='None':
            print('No presentation style provided')
        else:
            print('Invalid presentation style:', pres)
        pres=''

        import os
        import re

        if not os.path.isfile('./cnf.txt'):
          with open('./cnf.txt', 'w') as f:
              f.write(f, '')
        with open('./cnf.txt') as f:
            txt = f.read()
        for m in re.compile('(?<=presentation\=).*?(?=$|\n)').findall(txt):
            pres+=m
        if len(pres) > 1:
            print(pres, 'found in cnf.txt')
        while pres not in presDict.values():
            print(f'{pres} not valid presentation style')
            pres = str(input(
               'Please provide presentation style:\n1 for table \n2 for plot (default)'+ 
               '\n\n(You can change later from \'cnf.txt\')'
               )).lower() or 'plot'
            if pres == '' or pres == 'None':
               pres = '2'
            if pres in presDict.keys() or pres in presDict.values():
              if pres in presDict.keys():
                pres = presDict[pres]
              import re
              import functools
              newTxt = re.compile(r'(?=^|\n)presentation\=.*(?=\n|$)').sub('',txt) + f'presentation={pres}\n'
              with open('./cnf.txt','w') as f:
                    f.write(newTxt)
    print(f'{pres} style choosen for presentation.')
    return pres

def confLng(refLng):
    lngDict={'1':'arabic','2':'bengali','3':'english'}
    if refLng not in lngDict.values():
      if refLng in lngDict.keys():
          refLng=lngDict[refLng]
      else:
        if refLng=='' or refLng=='None':
            print('No tafsir language provided')
        else:
            print('Invalid tafsir language:', refLng)
        refLng=''
        import re
        with open('./cnf.txt') as f:
            txt = f.read()
        for m in re.compile('(?<=refLng\=).*(?=$|\n)').findall(txt):
            refLng+=m
        if len(refLng) > 0:
            print(refLng, 'found in cnf.txt')
        while refLng not in lngDict.values():
            print('no valid tafsir language!')
            refLng = str(input(
               'Please choose tafsir language:\n1 for Arabic \n2 for Bengali \n3 for English (default) '+
               '\n\n(You can change later from \'cnf.txt\')'
               )).lower()
            if refLng == '' or refLng == 'None':
               refLng = '3'
            if refLng in lngDict.values() or refLng in lngDict.keys():
              if refLng in lngDict.keys():
                refLng=lngDict[refLng]
              import re
              newTxt = re.compile(r'(?=^|\n)refLng\=.*(?=\n|$)').sub('',txt) + f'refLng={refLng}\n'
              with open('./cnf.txt','w') as f:
                  f.write(newTxt)
    print(f'{refLng} language choosen for reference.')

    tafsDict={"arabic":"ar-tafsir-al-tabari","bengali":"bn-tafseer-ibn-e-kaseer","english":"en-tafisr-ibn-kathir"}
    return tafsDict[refLng]



def getSorter():
    
    
    """ to tweak the sorter tweak the "surOrd.tsv" file manually """

    import os
    import json
    import csv
    with open('qdict.json') as f:
        qStr = f.read()
    qDict = json.loads(qStr)

    loadedFromDict = False

    if os.path.isfile('sorter.json'):
        print("'sorter.json' found'")
        if os.path.getctime('sorter.json') > os.path.getctime('surOrd.tsv'):
            with open('sorter.json') as f:
                sortStr = f.read()
                # print(f"in 'sorter.json': \n\n{sortStr}")
            try:
                sorter = json.loads(sortStr)
                print('last item in sorter:', sorter[-1])
                if len(sorter) == 6236:
                    loadedFromDict = True
                    print(f"successfully loaded sorter of length {len(sorter)} from 'sorter.json'")
                else:
                    print(f"length of sorter is {len(sorter)} (not equal to 114)")
                    del sorter
            except:
                print("failed to load sorter from 'sorter.json'")
        else:
            print("'surOrd.tsv' was modified. \nCreating new sorter")

    if not loadedFromDict:
        print("creating sorter from 'surOrd.tsv'")
        with open('surOrd.tsv') as f:
            surOrd = [row for row in csv.DictReader(f, delimiter='\t') ]

        sorter = [''] * 6236
        bef = {}
        aft = {}
        befaft = []

        for v in surOrd:
            s=v["surah"]
            if "exception" in v.keys():
                exs = v["exception"]
                if type(exs) == type(''):
                    exs = json.loads(exs)
                if len(exs) > 0:
                    for ex in exs:
                        ar = ex["ayah_range"].split('-')
                        al = ar if len(ar) == 1 else list(range(int(ar[0]),int(ar[1])+1)) if len(ar) == 2 else []
                        if "before" in ex.keys():
                            if ex["before"] != '':
                                if ex["before"] not in bef.keys():
                                    bef[ex["before"]]=[]
                                for ay in al:
                                    bef[ex["before"]].append(f'{s}:{ay}')
                                    befaft.append(f'{s}:{ay}')
                        if "after" in ex.keys():
                            if ex["after"] != '':
                                if ex["after"] not in aft.keys():
                                    aft[ex["after"]]=[]
                                for ay in al:
                                    aft[ex["after"]].append(f'{s}:{ay}')
                                    befaft.append(f'{s}:{ay}')

        i = 0

        for v in surOrd:
            s=v["surah"]
            for a in range(1, qDict[s]["verse_count"]+1):
                s_a= f'{s}:{a}'
                if s_a in bef.keys():
                    for sa in bef[s_a]:
                        sorter[i] = sa
                        i += 1
                if s_a not in befaft:
                    sorter[i] = s_a
                    i += 1
                if s_a in aft.keys():
                    for sa in aft[s_a]:
                        sorter[i] = sa
                        i += 1

        with open(f'sorter.json', 'w') as f:
            f.write(json.dumps(sorter))
    
    return sorter



def dataGrabber(
    rt,
    flt=''
  ):

  '''Grabs data from corpus.quran.com & formats them'''

  flt=str(flt).lower()
  import requests
  # import html2text
  from bs4 import BeautifulSoup
  import re
  import json
  import csv

  def getTbl(grabhtmlPara):
    soup = BeautifulSoup(
      grabhtmlPara,
      'lxml' 
    )

    tblsRet = soup.find_all(
      "table",
      {"class":"taf"}
    )

    return tblsRet

  links = [
      "https://corpus.quran.com/qurandictionary.jsp?q=",
      "https://corpus.quran.com/search.jsp?q=root%3A",
      "https://corpus.quran.com/search.jsp?q=lem%3A",
      "https://corpus.quran.com/search.jsp?q=stem%3A",
      "https://corpus.quran.com/search.jsp?q=",
      ]

  poss = set()
  tblCumul = []
  instLst=[]
  flnm = re.sub('([A-Z])','\\1?', rt)

  propDat = False
  import os
  if f'{flnm}.tsv' in os.listdir(f'data/roots/'):
    print(f"file found for {rt}")
    try:
      with open(f'data/roots/{flnm}.tsv') as f:
        print(f"loading data/roots/{flnm}.tsv")
        instLst = [row for row in csv.DictReader(f, delimiter='\t') ]
      #   tmpDat = json.loads(f.read())
      # if type(tmpDat) == type([]):
      #   if len(tmpDat) > 0:
      #     if tmpDat[0] == tmpDat["surah:ayah","position","word","meaning","ayah_link"]:
      #       propDat = True    
      #       instLst = tmpDat
      #       print(f"instLst loaded from 'data/roots/")
      #   instLst = tmpDat
        print(f"Successfully loaded data from 'dat/roots/{flnm}.tsv'")
        propDat = True
    except:
      propDat = False
  if not propDat:
    print(f"proper data not found for {rt}")
    tblAgg = []
    for lnk in links:
      if lnk == 'https://corpus.quran.com/qurandictionary.jsp?q=':
        grabhtml = requests.get(f"{lnk}{rt}").text
        tbls = getTbl(grabhtml)
      else:
        pgs = []
        grabhtml = requests.get(f"{lnk}{rt}").text
        tbls = getTbl(grabhtml)
        if '>\nResults <b>' in grabhtml:
          matches = re.findall(">\nResults <b>\d*</b> to <b>\d*</b> of <b>(\d*)</b>", grabhtml)
          if len(matches) > 0:
            pgFlt = int(matches[0])/50
            pgCount = int(pgFlt) + 1 if int(matches[0]) % 50 != 0 else int(pgFlt)
            # print(f"page count in {lnk} is: {pgCount}")
            # print(type(pgCount), pgCount)
            pgs = list(map(lambda x : f'&page={x}', list(range(2,pgCount+1))))

          for pg in pgs:
            grabhtml = requests.get(f"{lnk}{rt}{pg}").text
            tbls += getTbl(grabhtml)
            # print(f"length of grabhtml is: {len(grabhtmlNew)}")
            # grabhtml += grabhtmlNew
            # print(f"length of grabhtml after adding is: {len(grabhtml)}")

      # print(f"\nnumber of tables found in {lnk} for {rt} is: {len(tbls)}")
      # print(f"{tbls}\n")

      for tbl in tbls:
        # print(tbl)
        tblAgg += tbl

      # print(len(tblAgg))

      if len(tblAgg) > 0:
        # print(f"1st row of Table aggregate for {lnk} for {rt} is: {tblAgg[0].find_all('td')}")
        if 'adam' in tblAgg[0].find_all('td')[1].get_text().lower():
          if rt.lower() != 'adam' and rt != 'A^Edam':
            # print("no results")
            tblAgg = []

      # print(f"number of instances of {rt} in {lnk}: {len(tblAgg)}")
      # print(tblAgg)

      tblCumul += tblAgg
      # print(f"total number of instances so far of {rt} without removing duplicates: {len(tblCumul)}")

      for rw in tblCumul:
        row = [ fld.get_text() for fld in rw.find_all("td") ]
        # row = []
        # for fld in rw:
        #   row.append(fld.get_text())
          
        # print(row)
        pos = row[0].split(' ')[0].strip('()')
        # print(pos)
        if pos not in poss:
          # print(posSplit)
          posSplit = pos.split(':')
          # print(posSplit)
          instLst.append({
              "surah:ayah": f'{posSplit[0]}:{posSplit[1]}',
              "position": int(posSplit[2]), 
              "word": row[0].split(' ')[1], 
              "meaning": row[1],
              "ayah_link": row[2]
          })
          
          poss.add(pos)

      # print(f"number of unique instances upto {lnk}: {len(poss)} or {len(instLst)}")
    
    # with open(f'data/roots/{rt}', 'w') as f:
    #   print("writing to data/roots")
    #   f.write(
    #     json.dumps(instLst)
    #   )
    list_header = ['surah:ayah', 'position', 'word', 'meaning', 'ayah_link']

    with open(f'data/roots/{flnm}.tsv', 'x') as f:
      print(f"writing {rt} to 'data/roots/{flnm}.tsv'")
      writer = csv.DictWriter(f, delimiter='\t', fieldnames=list_header)
      writer.writeheader()
      for datum in instLst:
        writer.writerow({
          list_header[0] : datum['surah:ayah'],
          list_header[1] : datum['position'],
          list_header[2] : datum['word'],
          list_header[3] : datum['meaning'],
          list_header[4] : datum['ayah_link'],
        })
    
    
    # print(len(instLst))

  return instLst

    # import pandas as pd

    # pd.set_option('display.max_rows', None)
    # pd.set_option('display.max_colwidth', None)

    # df = pd.DataFrame(columns = ["surah:ayah","position","word","meaning","ayah_link"])
    # df = pd.concat([df,pd.DataFrame.from_records(data)],
    #                 axis=0
    #                 )
    # df = df.drop_duplicates(['surah:ayah','position'])
    # # df = df.drop(['position'], axis=1)
    # df = df[df['meaning'].str.contains(flt, case=False)]
    # df["query"] = f'{rt} ({flt})'

    # return df.sort_values(["surah:ayah","position"])


def getColMap(dicti):
    import numpy as np
    colMap = {}
    leng = len(dicti)
    lwrLmt = 100
    uprLmt = 250
    p = np.linspace(lwrLmt,uprLmt,num=leng)
    for idx in range(1,leng+1):
      # n1=rand.randn()
      # n2=rand.randn()
      # i1=rand.randint(0,50)
      # i2=rand.randint(0,50)
      # clr=f"rgb({50+(100/leng)*idx})"
      # colMap[df["query"].unique()[idx]] = f"rgb({clr},{clr},{clr})" 
    #   rd = int(p[idx-1])
    #   radialDist = (rd - lwrLmt) if (rd - lwrLmt) < (uprLmt - rd) else (uprLmt - rd)
      colMap[f"{list(dicti.keys())[idx-1]} ({list(dicti.values())[idx-1]})"] = f'rgb({int(p[idx-1])},{int(p[-idx]-30)},20)' 
    #   colMap[f"{list(dicti.keys())[idx-1]} ({list(dicti.values())[idx-1]})"] = f'rgb({rd},{gn},{bl})' 
    #   print(f'rgb({int(p[idx-1])},{int(p[-idx]-50)},25)' )
    return colMap


def filtDown(rt,flt):
    import re
    instLst = dataGrabber(rt,flt)
    instLstFiltered =  list(filter( lambda row : len(re.compile(str(flt).lower()).findall(row["meaning"].lower())) > 0 or len(re.compile(str(rt).lower()).findall(row["meaning"].lower())), instLst))
    # instLstFiltered = [ { **row , "query" : f"{rt} ({flt})"} for row in instLstFiltered ]
    return instLstFiltered

def intersct(rtAgg,flAgg=''):
    rtList = rtAgg.split(' ')
    if len(rtList) > 1:
        flList = flAgg.split(' ')
        rtFlAgg = [ { rtList[i] : flList[i]} for i in range(len(rtList)) ]
        # rtFlAgg = { **dicti for dict in rtFlList[1] }
        # return rtFlAgg
        instLstAgg = []
        surahAyahAggSet = set()
        for dicti in rtFlAgg:
            instLst = filtDown(list(dicti.keys())[0],list(dicti.values())[0])
            surahAyahList = [ inst["surah:ayah"] for inst in instLst ]
            if surahAyahAggSet == set([]):
                surahAyahAggSet = set(surahAyahList)
            else:
                surahAyahAggSet = surahAyahAggSet.intersection(surahAyahList)
            instLstAgg += instLst
        
        instLstFlt = list(filter(
            lambda x: x["surah:ayah"] in surahAyahAggSet,
            instLstAgg
        ))
        instDictInc = {}
        for inst in instLstFlt:
            surahAyah = inst["surah:ayah"]
            if surahAyah not in instDictInc.keys():
                instDictInc[surahAyah] = {
                    "position": inst["position"],
                    "word": inst["word"],
                    "meaning": inst["meaning"],
                    "ayah_link" : inst["ayah_link"],
                    "query": f"{rtAgg} ({flAgg})"
                }
            else:
                instDictInc[surahAyah]["word"] = instDictInc[surahAyah]["word"] + ' ' + inst["word"]
                instDictInc[surahAyah]["meaning"] = instDictInc[surahAyah]["meaning"] + ' ' + inst["meaning"]

        instLstInc = [ {"surah:ayah":k, **v } for k, v in instDictInc.items() ]
        return instLstInc
    
    elif len(rtList) == 1:
        instLstFlt = filtDown(rtAgg,flAgg)
        instLstInc = [ { **rec, "query": f"{rtAgg} ({flAgg})" } for rec in instLstFlt ]
        return instLstInc
    
    else:
        print("please provide at least one root/word")

def aggregLsts(dicti,tafs):
    # lnkStyle = ' '
    fontSize = '18'
    fontCol = 'rgb(0,0,150)'
    shPx = str(int(fontSize)/100*0)
    shCol = '#000000'
    bgCol = 'rgb(220,220,250)'
    txtShad = ''
    # txtShad = f'text-shadow:{shPx}px {shPx}px 0 {shCol}, {shPx}px -{shPx}px 0 {shCol}, -{shPx}px -{shPx}px 0 {shCol}, -{shPx}px {shPx}px 0 {shCol};'
    # lnkStyle = "style='background-color:rgb(250,250,250);font-size:30px;color:rgb(0,0,150);-webkit-text-stroke-width:5px;-webkit-text-stroke-color:white' "
    lnkStyle = f"style='background-color:{bgCol};font-size:{fontSize}px;color:{fontCol};{txtShad}' "
    # lnkStyle = "style='color:rgb(250,250,250);-webkit-text-stroke-width:1px;-webkit-text-stroke-color:rgb(0,0,0);' "
    instLstAgg = []
    for rt in dicti.keys():
        # instLst = filtDown(rt,dicti[rt])
        # instLst = intersct(rt,dicti[rt])
        # instLstAgg += instLst
        rtOptLs = rt.split('/')
        flOptLs = dicti[rt].split('/')
        for i in range(len(rtOptLs)):
            instLst = intersct(rtOptLs[i],flOptLs[i])
            if len(rtOptLs) > 1:
                instLst = [ { **inst, "query": f"{rt} ({dicti[rt]})"} for inst in instLst  ]
            instLstAgg += instLst
    instLstAgg = [ { 
        **row, 
        "ayah_link": f"<a {lnkStyle}href='https://quran.com/{row['surah:ayah']}/tafsirs/{tafs}'>{row['ayah_link']}</a>"
        # "ayah_link": f"<a href='https://quran.com/{row['surah:ayah']}/tafsirs/{tafs}'>{row['ayah_link']}</a>"
        } for row in instLstAgg ]
    print(f"\ntotal {len(instLstAgg)} instances found")
    return instLstAgg


def tabular(df,colMap,sorter):
    import pandas as pd
    # print(df)

    # for rt in dicti.keys():
    #     instLst = aggregLsts(rt,dicti[rt])
    #     dfNew = pd.DataFrame.from_records(instLst)
    #     df = pd.concat([df, dfNew], axis=0)

    print(f'dataframe length: {len(df)}')
    # df.drop(columns=[
    # #  "query",
    #     "index"
    #     ],
    #     inplace=True
    # )

    compareDict = {}
    for i in range(len(sorter)):
        compareDict[sorter[i]]=i

    df.insert( 0, 'verses_before',    list(
        map(
            lambda x: compareDict[x],
            # df["surah"]
            df["surah:ayah"]
            )
        )
    )

    from IPython.core.display import HTML

    def colo(s):
        # print(s)
        return [
            f'background-color: {colMap[s["query"]]};'
            + 'foreground-color: black;'
            + 'color: black;'
            + 'opacity: 1;' 
        ] * len(s)
    
    return HTML(df.style.apply(
            colo , axis=1
        ).to_html(render_links=True,escape=False,index=False)
    )



def plotDf(df,colMap,sorter):
    import plotly.express as px
    # import plotly.graph_objects as go
    # from plotly.subplots import make_subplots
    # from plotly.offline import iplot, init_notebook_mode
    # init_notebook_mode()
    df["ayah_link"] = list(df["surah:ayah"]) + df["ayah_link"]
    df.reset_index(inplace=True)
    fig = px.scatter(
        df,
        x='surah:ayah',
    #  y='ayah_link',
        y='index',
        hover_data={
        'ayah_link':True,
        'query': False, 
        'surah:ayah': False,
        'index': False
        },
        color='query',
    #  color_continuous_scale=["green","yellow","orange","red"],
        # color_discrete_map=colMap,
        height=((len(df))*7)+200,
        # height=1200,
        width=(len(sorter))/8+500,
    )

    # fig = make_subplots(
    #     specs=[[{"secondary_y": True}]]
    # )

    # # fig.layout=go.Layout(clickmode='event+select')
    
    fig.update_layout(
    #  hovermode=False,
        clickmode='event+select',
        hoverdistance=-1,
        hoverlabel=dict(
           font=dict(
              size=15,
              color='rgb(0,0,0)',              
           ),
            # font_size=15,
            # font_color='rgb(0,0,0)',
            bgcolor = 'rgb(220,220,250)'
        )
    #  itemclick='toggle'
    )

    # for rt in dicti:
    #     if rt != '' and rt != None:
    #       tbl = dataGrabber(tafs,rt,dicti[rt])
    #       fig.add_trace(
    #           go.Scatter(
    #               y=tbl.ayah_link,
    #               x=tbl['surah:ayah'],
    #               name=rt +  f' ({dicti[rt]})' if dicti[rt] != None or dicti[rt] != '' else '',
    #               mode='markers',
    #               # customdata=dataGrabber(tafs,rt,dicti[rt]).ayah_link,
    #               hoverinfo='y+x'
    #               # marker=dict(
    #               # color='rgb(34,163,192)'
    #               # )
    #           ),
    #           secondary_y=True
    #       )
    fig.update_xaxes(
        categoryorder='array',
        categoryarray=sorter,
        range=[0,len(sorter)],
        title=" (earlier)   -->  'Surah:Ayah' (Chronologically Ordered)  -->   (latter)"
    )
    fig.update_yaxes(
    #  showticklabels=False,
    #  range=[0,len(df)],
        title=''
    )
    fig.show()



def sortchron(dicti={},refLng='',pres=''):

    if type(dicti) != type({}):
        print("Invalid root-filter key value pairs")
        dicti={}
    if dicti=={}:
        finished=False
        while finished==False:
            inpLs=str(input(
                """
                Enter comma-separated list of
                '::' double colon-separated pairs of
                word/root and meaning-filter regex like:

                \'$Tn::devil,rwH::(?:spirit|soul)\'

                or \'sHr,jnn::jinn\n\'
                """
                )
            ).split(',')
            if type(inpLs) == type([]) and len(inpLs) >= 1:
              for obj in inpLs:
                pair = obj.strip().split('::')
                if len(pair) == 2:
                  dicti[pair[0]]=pair[1]
                  finished=True
                if len(pair) == 1:
                  dicti[pair[0]]=''
                  finished=True

    pres = confPres(pres=pres)
    tafs = confLng(refLng=refLng)
    sorter = getSorter()
    colMap = getColMap(dicti)
    instLstAgg = aggregLsts(dicti,tafs)

    import pandas as pd
    df = pd.DataFrame(instLstAgg,columns = ["surah:ayah","position","word","meaning","ayah_link","query"])
    df['surah:ayah'] = pd.Categorical(df['surah:ayah'], categories=sorter, ordered=True)
    df.sort_values(["surah:ayah","position"],inplace=True)
    df.reset_index(drop=True,inplace=True)
    # df.reset_index(inplace=True)

    if pres == "table":
        return tabular(df,colMap,sorter)
    if pres == "plot":
        plotDf(df,colMap,sorter)