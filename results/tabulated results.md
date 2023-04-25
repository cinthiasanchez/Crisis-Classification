# Results by Target Language and Domain

We show the F1-score below. This score is the average of 5 executions. For each target, the best data representation is highlighted in bold and the
best scenario is also in italic.

## English


|   Domain   |          Scenario          |  LF  |  MT+GloVe  | MUSE |  MUSE+LF | mBERT |   MT+BERT  |    XLM-R   |    XLM-T   |
|:----------:|:--------------------------:|:----:|:----------:|:----:|:--------:|:-----:|:----------:|:----------:|:----------:|
| Earthquake | Monolingual & Monodomain   | 0.77 |    0.82    | 0.82 |   0.82   |  0.81 |    0.81    |  **0.84**  |    0.82    |
|            | Monolingual & Cross-Domain | 0.84 |    0.87    | 0.86 |   0.87   |  0.88 | **_0.89_** | **_0.89_** | **_0.89_** |
|            | Monolingual & Multi-Domain | 0.83 |    0.87    | 0.85 |   0.86   |  0.87 | **_0.89_** |    0.88    |    0.88    |
| Explosion  | Monolingual & Cross-Domain | 0.89 | **_0.92_** | 0.86 |   0.89   |  0.87 |    0.86    |    0.90    | **_0.92_** |
| Flood      | Monolingual & Monodomain   | 0.84 |    0.88    | 0.88 | **0.90** |  0.85 |    0.88    |    0.89    |    0.89    |
|            | Monolingual & Cross-Domain | 0.82 |    0.86    | 0.84 |   0.86   |  0.84 |  **0.87**  |    0.86    |  **0.87**  |
|            | Monolingual & Multi-Domain | 0.83 |    0.88    | 0.87 |   0.88   |  0.86 |  **0.89**  |  **0.89**  |  **0.89**  |


## Spanish



|   Domain   |           Scenario           |  LF  | MT+GloVe | MUSE | MUSE+LF |   mBERT  |   MT+BERT  |    XLM-R   |    XLM-T   |
|:----------:|:----------------------------:|:----:|:--------:|:----:|:-------:|:--------:|:----------:|:----------:|:----------:|
| Earthquake | Monolingual & Monodomain     | 0.73 |   0.80   | 0.81 |   0.80  |   0.80   |  **0.83**  |    0.79    |    0.81    |
|            | Monolingual & Cross-Domain   | 0.66 |   0.72   | 0.75 |   0.75  |   0.78   |  **0.79**  |    0.75    |    0.77    |
|            | Cross-Lingual & Monodomain   | 0.68 |   0.79   | 0.75 |   0.75  |   0.76   |  **0.83**  |    0.80    |    0.80    |
|            | Cross-Lingual & Cross-Domain | 0.78 |   0.84   | 0.81 |   0.81  |   0.84   | **_0.86_** |    0.85    |    0.84    |
|            | Cross-Lingual & Multi-Domain | 0.77 |   0.84   | 0.80 |   0.81  |   0.84   | **_0.86_** |    0.84    |    0.84    |
|            | Multilingual & Multi-Domain  | 0.75 |   0.84   | 0.74 |   0.77  |   0.79   | **_0.86_** |    0.83    |    0.83    |
| Explosion  | Monolingual & Cross-Domain   | 0.73 |   0.77   | 0.69 |   0.72  |   0.76   |    0.69    |    0.77    |  **0.78**  |
|            | Cross-Lingual & Monodomain   | 0.75 | **0.84** | 0.64 |   0.74  |   0.72   |    0.79    |    0.79    |    0.65    |
|            | Cross-Lingual & Cross-Domain | 0.73 |   0.81   | 0.74 |   0.77  | **0.82** |    0.77    |    0.75    |    0.77    |
|            | Cross-Lingual & Multi-Domain | 0.74 | **0.82** | 0.74 |   0.78  | **0.82** |  **0.82**  |    0.80    |    0.76    |
|            | Multilingual & Multi-Domain  | 0.76 |   0.83   | 0.75 |   0.79  |   0.83   |    0.83    | **_0.85_** | **_0.85_** |


## Italian


|   Domain   |            Scenario            |  LF  | MT+GloVe |   MUSE   |  MUSE+LF |   mBERT  |   MT+BERT  |    XLM-R   | XLM-T |
|:----------:|:------------------------------:|:----:|:--------:|:--------:|:--------:|:--------:|:----------:|:----------:|:-----:|
| Earthquake | Monolingual & Monodomain       | 0.67 |   0.72   | **0.75** |   0.72   |   0.70   |    0.74    |    0.72    |  0.70 |
|            | Monolingual &   Cross-Domain   | 0.67 |   0.73   |   0.77   |   0.76   | **0.78** |    0.76    |    0.77    |  0.78 |
|            | Cross-Lingual &   Monodomain   | 0.56 |   0.77   |   0.78   |   0.77   |   0.75   |  **0.79**  |    0.70    |  0.63 |
|            | Cross-Lingual &   Cross-Domain | 0.63 |   0.78   | **0.79** |   0.76   |   0.68   |    0.77    |    0.77    |  0.73 |
|            | Cross-Lingual &   Multi-Domain | 0.62 |   0.78   | **0.80** |   0.77   |   0.71   |    0.78    |    0.76    |  0.71 |
|            | Multilingual &   Multi-Domain  | 0.67 |   0.79   |   0.76   |   0.79   |   0.73   | **_0.82_** |    0.75    |  0.72 |
|    Flood   | Monolingual & Cross-Domain     | 0.72 |   0.72   |   0.74   |   0.78   |   0.76   |    0.77    |  **0.81**  |  0.79 |
|            | Cross-Lingual &   Monodomain   | 0.79 |   0.81   |   0.73   |   0.82   |   0.53   |    0.68    |  **0.83**  |  0.54 |
|            | Cross-Lingual &   Cross-Domain | 0.74 |   0.75   |   0.73   |   0.76   |   0.65   |    0.74    |  **0.82**  |  0.79 |
|            | Cross-Lingual &   Multi-Domain | 0.77 |   0.79   |   0.75   |   0.80   |   0.63   |    0.73    | **_0.84_** |  0.78 |
|            | Multilingual &   Multi-Domain  | 0.75 |   0.81   |   0.79   | **0.83** |   0.78   |    0.80    |    0.79    |  0.75 |
