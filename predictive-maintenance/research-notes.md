# Research notes — predictive maintenance

This first selection assumes that the proposed work is a data-driven predictive-maintenance system using condition-monitoring or operational data, machine-learning models, and actionable maintenance outputs. The exact relation should be refined once the proposed system and dataset are specified.

## Evidence matrix

| Key | Database and access | Setup | Main finding | Limitation | Role in the article |
|---|---|---|---|---|---|
| meitz2025pdmframework | Elsevier/ScienceDirect; open access, CC BY 4.0 | Structured review of 249 publications, classified into 9 categories and 73 attributes | Organizes condition monitoring, fault detection, degradation, scheduling, data handling, prognostic techniques, and evaluation; highlights complexity, benchmark-data, and interpretability challenges | It is a review and does not provide an experimental comparison of model performance | Establishes the research landscape and motivates an integrated, carefully evaluated architecture |
| gupta2023baggage | Elsevier/ScienceDirect; publisher version is paywalled, accepted postprint is freely available through Cardiff University's repository | Live IoT vibration data from eight identical airport baggage-handling S-Lifts; anomaly detection, data cleaning, text processing, and supervised ML | Random Forest outperformed logistic regression, multilayer perceptron, and SVM for the reported motor-gearbox classification, with precision, recall, and F1 of 0.86 | Cleaning relies mainly on RMS; run-to-failure prognosis was left for future work; training and testing ignored conveyor identity, limiting transferability | Supports the need to treat sensor noise, missing failure histories, data labeling, and deployment constraints explicitly |
| burmeister2023production | IEEE Xplore/IEEE Access; open access, CC BY-NC-ND 4.0 | 227,996 production/inspection observations and 29 variables; Bayesian networks and classification trees | The interpretable CT RUS model achieved the highest F1 score and accuracy among the evaluated models, translating predictions into production rules | The case uses one company's production process and a highly imbalanced response; generalization requires external validation | Supports interpretable outputs and the use of operational data beyond raw sensor streams |

## Selection rationale

Together, the papers cover complementary layers of a predictive-maintenance system: field-wide requirements, real-world sensing and data preparation, and interpretable prediction. They also make the central caution clear: benchmark accuracy alone is insufficient without attention to noise, class imbalance, labeling, deployment, and transferability.

## Primary records

- Meitz et al.: https://doi.org/10.1016/j.cie.2025.111193
- Gupta et al.: https://doi.org/10.1016/j.cie.2023.109033
- Gupta et al. accepted manuscript: https://orca.cardiff.ac.uk/id/eprint/156892/
- Burmeister et al.: https://doi.org/10.1109/ACCESS.2023.3315842
- Burmeister et al. open version: https://vbn.aau.dk/ws/files/573764754/Exploration_of_Production_Data_for_Predictive_Maintenance_of_Industrial_Equipment_A_Case_Study.pdf
