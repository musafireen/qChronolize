# qChronolyze
Try on google <a href="https://colab.research.google.com/drive/1Su624t2FdQdWnnZTdl1_pz2bH7DujU2G?usp=sharing" target="_blank">Colab<a>



<a href="https://ibb.co/vZjz4ZZ"><img src="https://i.ibb.co/vZjz4ZZ/vlcsnap-2024-04-23-21h02m52s708.png" alt="vlcsnap-2024-04-23-21h02m52s708" border="0"></a>  <a href="https://ibb.co/p0YPPRr"><img src="https://i.ibb.co/p0YPPRr/vlcsnap-2024-04-23-21h03m12s122.png" alt="vlcsnap-2024-04-23-21h03m12s122" border="0"></a> 

<a href="https://ibb.co/5khCqsD"><img src="https://i.ibb.co/5khCqsD/vlcsnap-2024-04-23-21h03m40s994.png" alt="vlcsnap-2024-04-23-21h03m40s994" border="0"></a>  <a href="https://ibb.co/jMMVvx0"><img src="https://i.ibb.co/jMMVvx0/vlcsnap-2024-04-23-21h02m44s809.png" alt="vlcsnap-2024-04-23-21h02m44s809" border="0"></a>

1) Shows at what point in the composition of Quran particular words and concepts were introduced according to traditional account
2) Visualizes relative frequency of multiple words, or frequency of single word in different periods
3) both tabular and scatterplot visualization
4) you can search by either words, or word roots 
5) Clickable data points & hyperlinks for context of each instance of a word used in the quran ([Tafsir](https://quran.com/2:102/tafsirs/en-tafisr-ibn-kathir) in 3 languages: Arabic, English & Bengali)

## transliteration scheme
if you are searching by word root, follow [this scheme](https://corpus.quran.com/java/buckwalter.jsp) for transliteration

## corpus

[corpus.quran.com](https://corpus.quran.com/qurandictionary.jsp?q=klm) gathers all the data about individual words, but lacks chronological data, and comparing functionality.

## chronological order:
The chronology is based on traditional [Ibn Abbas account](https://tanzil.net/docs/revelation_order)

if you are a researcher who uses a different chronology of surahs/verses you can tweak the "surOrd.tsv" file:
1) by manually moving around the lines for each surah, 
2) changing the values in "before"/"after" and "ayah_range" in "exception" fields.

