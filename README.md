This repository contains the measurements and analysis tools used in our study on `Performance evaluation of Private and Public Blockchains for
multi-cloud service federation`, presented at ICDCN '24.

## Authors

- Adam Zahir, Milan Groshev, Kiril Antevski, Carlos J. Bernardos, Constantine Ayimba, and Antonio de la Oliva from Universidad Carlos III de Madrid.

## Getting started

### Prerequisites

- Python 3.8 or later
- Pandas and Matplotlib libraries

### Running the analysis

1. **Merge and format data**: Use `merge_and_format_csv.py` to combine and format federation events data from both consumer and provider perspectives into a singular CSV file.
   
2. **Calculate mean values**: Execute `calculate_mean.py` to compute and compile mean start and end times across various test scenarios into singular CSV files.
   
3. **Plot results**: Execute `plot_figure_private_blockchain.py` and `plot_figure_private_vs_public_blockchain.py` to generate the figures presented in our study.



## Acknowledgments
This work has been partly funded by the European Commission Horizon Europe SNS JU DESIRE6G project, under grant agreement No.101096466, and the Spanish Ministry of Economic Affairs and Digital Transformation and the European Union-NextGenerationEU through the UNICO 5G I+D 6G-EDGEDT and 6G-DATADRIVEN.






