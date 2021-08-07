# Unified Multi-Crisis Dataset description
To create a multilingual and multi-domain crisis dataset, we consolidated data from the following 7 public sources, totaling 164,625 tweets:

- **CrisisLexT6 [1]:** English tweets from six crisis events in 2012 and 2013, occurring in USA, Canada, and Australia. These events belong to different crisis domains such as hurricane, bombing, tornado, explosion and flood. Tweets were labeled by relatedness with each event as *on-topic* or *off-topic*.

- **CrisisLexT26 [2]:** Tweets from 26 crises in 2012 and 2013, occurring in countries with different languages. Tweets were labeled by informativeness, information type and source. Regarding informativeness, tweets were labeled as *related and informative*, *related - but not informative*, *not related* or *not applicable*.

- **SoSItalyT4 [3]:** Italian tweets from four natural disasters that occurred in Italy between 2009 and 2014. These events specifically belong to the flood and earthquake crisis domains. According to the type of information tweets convey, they were labeled as *damage*, *no damage* or *not relevant*.

- **ChileEarthquakeT1 [4]:** Spanish tweets from the 2010 Chilean earthquake, labeled by relatedness with the event as *relevant* or *not relevant*.
    
- **CrisisNLP_R1 [5]:** Tweets from 19 crises that occurred in different countries between 2013 and 2015. Tweets were annotated with a set of categories according to the information type such as *Injured or dead people*, *Displaced people and evacuations*, *Infrastructure and utilities damage*, among others. We used both datasets, annotated by paid workers and annotated by volunteers.  

- **CrisisMMD [6]:** English tweets with images collected during seven natural disasters in 2017, occurring in different countries. These events belong to different crisis domains such as hurricane, earthquake, wildfire and flood. Tweets were labeled by informativeness (tweet or image), humanitarian categories (tweet or image), and damage severity (image). Regarding informativeness, tweets were labeled as *informative* or *not informative*.
    
- **Ecuador-Earthquake [7]:** Tweets in English and Spanish about the earthquake occurred in Ecuador in 2016. Tweets were labeled by relatedness with the event as *related* or *not related*.


## Language detection

As not all messages provided their language, we had to identify it. 
We used three text-based language detection libraries, which are [FastText](https://fasttext.cc/docs/en/language-identification.html), [LangID](https://github.com/saffsd/langid.py) and [langdetect](https://github.com/Mimino666/langdetect).
These were applied after removing urls, user mentions, hashtags, retweet symbols, emojis, emoticons and most symbols, while maintaining capitalization, numbers and specific punctuation marks (.,¡!¿?) to preserve the semantics for more accurate language detection.

The assigned language corresponds to the majority of votes considering the three detectors. Otherwise the language label is *no_agreement*.
In addition, we assigned the label *no_text* to those messages with clean text composed only of numbers, symbols or a single word with less than four characters because a text with these properties may not be sufficient to detect the language.

Most messages were detected as English (83.7\%), followed by Spanish (7.3\%) and Italian (4.3\%). In addition, there was no agreement in the detection of 2.2\% of the messages. 


| Language   ID |           Language           |  Tweets |
|:-------------:|:----------------------------:|:-------:|
|       en      |            English           | 137,743 |
|       es      |            Spanish           |  12,025 |
|       it      |            Italian           |  7,002  |
|       fr      |            French            |  1,144  |
|       pt      |          Portuguese          |   771   |
|       tl      |            Tagalog           |   502   |
|       ru      |            Russian           |   238   |
|       de      |            Deutsch           |   124   |
|       id      |          Indonesian          |   111   |
|       nl      |        Dutch, Flemish        |   101   |
|  no_agreement |     No language assigned     |  3,623  |
|    no_text    |     No language assigned     |   769   |
|     others    | Remaining detected languages |   472   |


## Crisis Categorization

We annotate each message according to the crisis dimensions of the event that it belongs to [2].

|  Hazard type  |    Category   |   Subcategory  |  Development  |   Spread  | Tweets |
|:-------------:|:-------------:|:--------------:|:-------------:|:---------:|:------:|
| Collapse      | Human-induced | Accidental     | Instantaneous | Focalized |  1,250 |
| Crash         | Human-induced | Accidental     | Instantaneous | Focalized |  1,234 |
| Derailment    | Human-induced | Accidental     | Instantaneous | Focalized |  2,999 |
| Explosion     | Human-induced | Accidental     | Instantaneous | Focalized | 12,004 |
| Fire          | Human-induced | Accidental     | Instantaneous | Focalized |  1,000 |
| Bombings      | Human-induced | Intentional    | Instantaneous | Focalized | 11,012 |
| Shooting      | Human-induced | Intentional    | Instantaneous | Focalized |  1,032 |
| Haze          | Mixed         | Others         | Progressive   | Diffused  |  1,000 |
| Viral disease | Natural       | Biological     | Progressive   | Diffused  |  3,512 |
| Landslide     | Natural       | Hydrological   | Instantaneous | Focalized |  4,492 |
| Wildfires     | Natural       | Climatological | Progressive   | Diffused  |  3,533 |
| Earthquake    | Natural       | Geophysical    | Instantaneous | Diffused  | 41,931 |
| Volcano       | Natural       | Geophysical    | Progressive   | Diffused  |    416 |
| Flood         | Natural       | Hydrological   | Progressive   | Diffused  | 31,923 |
| Cyclone       | Natural       | Meteorological | Progressive   | Diffused  |  2,601 |
| Hurricane     | Natural       | Meteorological | Progressive   | Diffused  | 19,578 |
| Tornado       | Natural       | Meteorological | Progressive   | Diffused  |  9,992 |
| Typhoon       | Natural       | Meteorological | Progressive   | Diffused  | 13,674 |
| Meteorite     | Natural       | Others         | Instantaneous | Focalized |  1,442 |


## References
[1] Alexandra Olteanu, Carlos Castillo, Fernando Diaz, and Sarah Vieweg. [CrisisLex: A lexicon for collecting and filtering microblogged communications in crises](https://crisislex.org/data-collections.html#CrisisLexT6). In Proceedings of the Eighth International Conference on Weblogs and Social Media, pages 376–385. AAAI, 2014.

[2] Alexandra Olteanu, Sarah Vieweg, and Carlos Castillo. [What to expect when the unexpected happens: Social media communications across crises](https://crisislex.org/data-collections.html#CrisisLexT26). In Proceedings of the 18th ACM Conference on Computer Supported Cooperative Work & Social Computing, page 994–1009. ACM, 2015.

[3] Stefano Cresci, Maurizio Tesconi, Andrea Cimino, and Felice Dell’Orletta. [A linguistically-driven approach to cross-event damage assessment of natural disasters from social media messages](https://crisislex.org/data-collections.html#SoSItalyT4). In Proceedings of the 24th International Conference on World Wide Web, page 1195–1200. ACM, 2015.

[4] Alfredo Cobo, Denis Parra, and Jaime Navón. [Identifying relevant messages in a Twitterbased citizen channel for natural disaster situations](https://crisislex.org/data-collections.html#ChileEarthquakeT1). In Proceedings of the 24th International Conference on World Wide Web, page 1189–1194. ACM, 2015.

[5] Muhammad Imran, Prasenjit Mitra, and Carlos Castillo. [Twitter as a lifeline: Humanannotated Twitter corpora for NLP of crisis-related messages](https://crisisnlp.qcri.org/lrec2016/lrec2016.html). In Proceedings of the Tenth International Conference on Language Resources and Evaluation, pages 1638–1643. ELRA, 2016.

[6] Firoj Alam, Ferda Ofli, and Muhammad Imran. [CrisisMMD: Multimodal Twitter datasets from natural disasters](https://crisisnlp.qcri.org/crisismmd). In Proceedings of the 12th International AAAI Conference on Web and Social Media (ICWSM), pages 465–473. AAAI, 2018.

[7] Johnny Torres and Carmen Vaca. [Cross-lingual perspectives about crisis-related conversations on Twitter](https://github.com/johnnytorres/twconvcrosslingual). In Companion Proceedings of The 2019 World Wide Web Conference, pages 255–261. ACM, 2019.
