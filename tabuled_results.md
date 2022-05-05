# Results by Target Language and Domain

We show the F1-score below. For each target, the best data representation is highlighted in bold and the
best scenario is also in italic.

## English


| Domain     |            Scenario           |   LF  | MT+      GloVe |  MUSE | MUSE      +LF |  BERT |
|------------|:-----------------------------:|:-----:|:--------------:|:-----:|:-------------:|:-----:|
| Earthquake | Monolingual & Monodomain     | 0.770 |      0.820     | 0.818 |   **0.822**   | 0.766 |
|            | Monolingual & Cross-Domain   | 0.841 |    **_0.873_** | 0.860 |     0.871     | 0.852 |
|            | Monolingual & Multi-Domain   | 0.835 |    **0.868**   | 0.853 |     0.863     | 0.844 |
| Explosion  | Monolingual & Cross-Domain   | 0.889 |    **_0.916_** | 0.862 |     0.892     | 0.871 |
| Flood      | Monolingual & Monodomain     | 0.837 |      0.877     | 0.877 |   **_0.899_** | 0.863 |
|            | Monolingual & Cross-Domain   | 0.824 |      0.860     | 0.843 |   **0.863**   | 0.844 |
|            | Monolingual & Multi-Domain   | 0.835 |      0.878     | 0.867 |   **0.885**   | 0.859 |


## Spanish

| Domain     | Scenario                      |    LF |    MT+GloVe |      MUSE | MUSE+LF |  BERT |
|------------|-------------------------------|------:|------------:|----------:|--------:|------:|
| Earthquake | Monolingual & Monodomain     | 0.731 |       0.800 | **0.805** |   0.801 | 0.793 |
|            | Monolingual & Cross-Domain   | 0.656 |       0.719 | **0.747** |   0.746 | 0.746 |
|            | Cross-Lingual & Monodomain   | 0.677 |   **0.794** |   0.749   |   0.754 | 0.737 |
|            | Cross-Lingual & Cross-Domain | 0.776 |   **0.842** |     0.807 |   0.811 | 0.833 |
|            | Cross-Lingual & Multi-Domain | 0.775 |   **0.841** |     0.796 |   0.805 | 0.813 |
|            | Multilingual & Multi-Domain  | 0.748 | **_0.844_** |     0.736 |   0.766 | 0.740 |
|  Explosion | Monolingual & Cross-Domain   | 0.725 |   **0.766** |     0.688 |   0.721 | 0.723 |
|            | Cross-Lingual & Monodomain   | 0.751 | **_0.836_** |     0.639 |   0.743 | 0.759 |
|            | Cross-Lingual & Cross-Domain | 0.726 |   **0.813** |     0.737 |   0.774 | 0.777 |
|            | Cross-Lingual & Multi-Domain | 0.736 |   **0.822** |     0.743 |   0.782 | 0.786 |
|            | Multilingual & Multi-Domain  | 0.758 |   **0.826** |     0.755 |   0.793 | 0.761 |


## Italian

|   Domain   |            Scenario           |   LF  |  MT+GloVe |     MUSE    |   MUSE+LF   |  BERT |
|:----------:|:-----------------------------:|:-----:|:---------:|:-----------:|:-----------:|:-----:|
| Earthquake | Monolingual & Monodomain     | 0.666 |   0.717   |  **0.750**  |    0.721    | 0.731 |
|            | Monolingual & Cross-Domain   | 0.666 |   0.727   |  **0.773**  |    0.762    | 0.733 |
|            | Cross-Lingual & Monodomain   | 0.562 |   0.769   |  **0.784**  |    0.772    | 0.758 |
|            | Cross-Lingual & Cross-Domain | 0.629 |   0.779   |  **0.795**  |    0.759    | 0.777 |
|            | Cross-Lingual & Multi-Domain | 0.619 |   0.781   | **_0.803_** |    0.773    | 0.785 |
|            | Multilingual & Multi-Domain  | 0.668 | **0.794** |    0.757    |    0.789    | 0.692 |
|    Flood   | Monolingual & Cross-Domain   | 0.724 |   0.717   |    0.740    |  **0.778**  | 0.728 |
|            | Cross-Lingual & Monodomain   | 0.786 |   0.811   |    0.732    |  **0.819**  | 0.645 |
|            | Cross-Lingual & Cross-Domain | 0.737 |   0.751   |    0.726    |  **0.761**  | 0.749 |
|            | Cross-Lingual & Multi-Domain | 0.765 |   0.794   |    0.746    |  **0.797**  | 0.737 |
|            | Multilingual & Multi-Domain  | 0.752 |   0.814   |    0.788    | **_0.826_** | 0.718 |
