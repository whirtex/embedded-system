# Research notes — predictive maintenance

This first selection assumes that the proposed work is a data-driven predictive-maintenance system using condition-monitoring or operational data, machine-learning models, and actionable maintenance outputs. The exact relation should be refined once the proposed system and dataset are specified.

## Evidence matrix

| Key | Study and access | Main evidence and limitation | Role in the article |
|---|---|---|---|
| `meitz2025pdmframework` | Structured review of 249 publications classified into 9 categories and 73 attributes. Elsevier/ScienceDirect; open access, CC BY 4.0. | Organizes condition monitoring, fault detection, degradation, scheduling, data handling, prognostic techniques, and evaluation. It is a review and does not provide an experimental comparison of model performance. | Establishes the research landscape and motivates an integrated, carefully evaluated architecture. |
| `gupta2023baggage` | Live IoT vibration data from eight identical airport baggage-handling S-Lifts; anomaly detection, data cleaning, text processing, and supervised ML. The accepted postprint is available through Cardiff University's repository. | Random Forest achieved precision, recall, and F1-score of 0.86 for the reported motor-gearbox classification. Cleaning relied mainly on RMS, and the study did not perform run-to-failure prognosis or account for conveyor identity in training and testing. | Supports explicit treatment of sensor noise, missing failure histories, data labeling, and deployment constraints. |
| `tormos2026hvacxai` | HVAC operational data from urban bus fleets, without reliable fault labels. Sensors are mapped onto the vapor-compression refrigeration cycle, an Isolation Forest flags deviations from the healthy baseline, and Kernel SHAP attributes each score to the contributing variables. Algorithms; open access, CC BY 4.0. | Attributions are grouped into physics-informed explanation families, so anomalies are read as refrigeration mechanisms rather than isolated variables. The setting is fleet telematics rather than stationary equipment, and the attribution step is too heavy for a microcontroller. | Supports learning the healthy baseline without labelled failures and reporting which measurement triggered each alert. |
| `gubbi2013iot` | Conceptual IoT architecture based on wireless sensor networks, the Internet, distributed computing, and embedded sensor/actuator nodes. Future Generation Computer Systems. | Describes the convergence needed to connect physical objects, collect context, and provide analytics through IoT services. It is a general IoT vision rather than an equipment-maintenance experiment. | Supports the general contextualization of embedded IoT monitoring. |
| `lin2017iot` | Survey of IoT architecture, enabling technologies, security/privacy, applications, and fog/edge computing. IEEE Internet of Things Journal. | Shows how processing near IoT devices can reduce latency and improve resilience in distributed applications. It is broad and does not prescribe the project's hardware or protocol. | Supports the embedded/IoT architecture and local or remote processing rationale. |
| `carvalho2019mlpdm` | Systematic literature review of machine-learning methods applied to predictive maintenance. Computers & Industrial Engineering; full-text access depends on institution. | Maps ML methods, results, challenges, and opportunities, emphasizing that application performance depends on method selection and data. It covers multiple industrial domains and is not specific to HVAC equipment. | Establishes the general predictive-maintenance and validation motivation. |
| `essakali2022hvac` | Systematic review of knowledge-based, physics-based, and data-driven predictive-maintenance algorithms for HVAC systems. Energy Reports; open access, CC BY 4.0. | Relates HVAC predictive maintenance to IoT sensors, historical data, health assessment, and failure anticipation. It is a review with no original experimental dataset and identifies data scarcity and RUL difficulty as challenges. | Provides the direct HVAC motivation and supports the project's cautious anomaly-detection scope. |

## Selection rationale

Together, the papers cover complementary layers of a predictive-maintenance system: field-wide requirements, real-world sensing and data preparation, and interpretable prediction. They also make the central caution clear: benchmark accuracy alone is insufficient without attention to noise, class imbalance, labeling, deployment, and transferability.

## Primary records

- Meitz et al.: https://doi.org/10.1016/j.cie.2025.111193
- Gupta et al.: https://doi.org/10.1016/j.cie.2023.109033
- Gupta et al. accepted manuscript: https://orca.cardiff.ac.uk/id/eprint/156892/
- Tormos et al.: https://doi.org/10.3390/a19070586
- Gubbi et al.: https://doi.org/10.1016/j.future.2013.01.010
- Lin et al.: https://doi.org/10.1109/JIOT.2017.2683200
- Carvalho et al.: https://doi.org/10.1016/j.cie.2019.106024
- Es-Sakali et al.: https://doi.org/10.1016/j.egyr.2022.07.130
- Tormos et al. open version: https://www.mdpi.com/1999-4893/19/7/586
