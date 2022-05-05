# Results by Target Language and Domain

We show the F1-score below. This score is the average of 5 executions. For each target, the best data representation is highlighted in bold and the
best scenario is also in italic.

## English


|   Domain   |           Scenario           |   LF  |  MT+GloVe |  MUSE |   MUSE+LF   |  BERT |   XLM-R   |    XLM-T    |
|:----------:|:----------------------------:|:-----:|:---------:|:-----:|:-----------:|:-----:|:---------:|:-----------:|
| Earthquake | Monolingual   & Monodomain   | 0.770 |   0.820   | 0.818 |    0.822    | 0.766 | **0.838** |    0.824    |
|            | Monolingual & Cross-Domain   | 0.841 |   0.873   | 0.860 |    0.871    | 0.852 |   0.888   | **_0.894_** |
|            | Monolingual & Multi-Domain   | 0.835 |   0.868   | 0.853 |    0.863    | 0.844 |   0.881   |  **0.884**  |
| Explosion  | Monolingual   & Cross-Domain | 0.889 | **0.916** | 0.862 |    0.892    | 0.871 |   0.902   |  **0.916**  |
| Flood      | Monolingual   & Monodomain   | 0.837 |   0.877   | 0.877 | **_0.899_** | 0.863 |   0.894   |    0.888    |
|            | Monolingual & Cross-Domain   | 0.824 |   0.860   | 0.843 |    0.863    | 0.844 |   0.861   |  **0.874**  |
|            | Monolingual & Multi-Domain   | 0.835 |   0.878   | 0.867 |    0.885    | 0.859 |   0.888   |  **0.894**  |


## Spanish


|   Domain   |           Scenario           |   LF  |  MT+GloVe |  MUSE | MUSE+LF |  BERT |   MT+BERT   |    XLM-R    |   XLM-T   |
|:----------:|:----------------------------:|:-----:|:---------:|:-----:|:-------:|:-----:|:-----------:|:-----------:|:---------:|
| Earthquake |  Monolingual   & Monodomain  | 0.731 |   0.800   | 0.805 |  0.801  | 0.793 |  **0.834**  |    0.794    |   0.812   |
|            |  Monolingual & Cross-Domain  | 0.656 |   0.719   | 0.747 |  0.746  | 0.746 |  **0.791**  |    0.754    |   0.774   |
|            |  Cross-Lingual & Monodomain  | 0.677 |   0.794   | 0.749 |  0.754  | 0.737 |  **0.832**  |    0.798    |   0.796   |
|            | Cross-Lingual & Cross-Domain | 0.776 |   0.842   | 0.807 |  0.811  | 0.833 | **_0.859_** |    0.847    |   0.841   |
|            | Cross-Lingual & Multi-Domain | 0.775 |   0.841   | 0.796 |  0.805  | 0.813 | **_0.859_** |    0.845    |   0.842   |
|            |  Multilingual & Multi-Domain | 0.748 |   0.844   | 0.736 |  0.766  | 0.740 |  **0.858**  |    0.831    |   0.829   |
|  Explosion | Monolingual   & Cross-Domain | 0.725 |   0.766   | 0.688 |  0.721  | 0.723 |    0.687    |    0.773    | **0.782** |
|            |  Cross-Lingual & Monodomain  | 0.751 | **0.836** | 0.639 |  0.743  | 0.759 |    0.792    |    0.793    |   0.649   |
|            | Cross-Lingual & Cross-Domain | 0.726 | **0.813** | 0.737 |  0.774  | 0.777 |    0.774    |    0.748    |   0.771   |
|            | Cross-Lingual & Multi-Domain | 0.736 | **0.822** | 0.743 |  0.782  | 0.786 |    0.817    |    0.796    |   0.765   |
|            |  Multilingual & Multi-Domain | 0.758 |   0.826   | 0.755 |  0.793  | 0.761 |    0.833    | **_0.854_** |   0.846   |


## Italian


|   Domain   |           Scenario           |   LF  | MT+GloVe |    MUSE   |  MUSE+LF  |  BERT |   MT+BERT   |    XLM-R    |   XLM-T   |
|:----------:|:----------------------------:|:-----:|:--------:|:---------:|:---------:|:-----:|:-----------:|:-----------:|:---------:|
| Earthquake | Monolingual   & Monodomain   | 0.666 |   0.717  | **0.750** |   0.721   | 0.731 |    0.742    |    0.723    |   0.700   |
|            | Monolingual & Cross-Domain   | 0.666 |   0.727  |   0.773   |   0.762   | 0.733 |    0.756    |    0.772    | **0.784** |
|            | Cross-Lingual & Monodomain   | 0.562 |   0.769  |   0.784   |   0.772   | 0.758 |  **0.795**  |    0.700    |   0.630   |
|            | Cross-Lingual & Cross-Domain | 0.629 |   0.779  | **0.795** |   0.759   | 0.777 |    0.770    |    0.769    |   0.726   |
|            | Cross-Lingual & Multi-Domain | 0.619 |   0.781  | **0.803** |   0.773   | 0.785 |    0.784    |    0.762    |   0.713   |
|            | Multilingual & Multi-Domain  | 0.668 |   0.794  |   0.757   |   0.789   | 0.692 | **_0.822_** |    0.747    |   0.716   |
|    Flood   | Monolingual   & Cross-Domain | 0.724 |   0.717  |   0.740   |   0.778   | 0.728 |    0.771    |  **0.807**  |   0.793   |
|            | Cross-Lingual & Monodomain   | 0.786 |   0.811  |   0.732   |   0.819   | 0.645 |    0.682    |  **0.833**  |   0.540   |
|            | Cross-Lingual & Cross-Domain | 0.737 |   0.751  |   0.726   |   0.761   | 0.749 |    0.739    |  **0.820**  |   0.793   |
|            | Cross-Lingual & Multi-Domain | 0.765 |   0.794  |   0.746   |   0.797   | 0.737 |    0.728    | **_0.841_** |   0.777   |
|            | Multilingual & Multi-Domain  | 0.752 |   0.814  |   0.788   | **0.826** | 0.718 |    0.802    |    0.794    |   0.753   |
