This project contains the measurements and analysis tools used in the conference paper entitled `Performance Evaluation of Multi-Cloud Service Federation using Private and Public Blockchains`, which was presented at [ICDCN 2024](https://cse.iitm.ac.in/~icdcn2024/). 

## Authors

- Adam Zahir, Milan Groshev, Kiril Antevski, Carlos J. Bernardos, Constantine Ayimba, and Antonio de la Oliva from Universidad Carlos III de Madrid (UC3M).

## Getting started

### Prerequisites

- Python 3.8 or later
- Pandas and Matplotlib libraries

### Files Structure

- **data**: Contains data obtained from the experiments.

- **scripts**: Contains the scripts used to generate the plots.

- **presentation**: Contains the PowerPoint presentation used in the ICDCN conference.

### Running the analysis

Go to `scripts` directory:

```bash
cd scripts
```

1. **Merge and format data**: Use `merge_and_format_csv.py` to combine and format federation events data from both consumer and provider perspectives into a singular CSV file.

```bash
python3 merge_and_format_csv.py
```

2. **Calculate mean values**: Execute `calculate_mean.py` to compute and compile mean start and end times across various test scenarios into singular CSV files. These files are located inside the mean directory.

```bash
python3 calculate_mean.py
```
   
3. **Plot results**: Execute `plot_figure_private_blockchain.py` and `plot_figure_private_vs_public_blockchain.py` to generate the figures presented in our study.

```bash
python3 plot_figure_private_blockchain.py
```

```bash
python3 plot_figure_private_vs_public_blockchain.py
```


## Acknowledgments
This work has been partly funded by the European Commission Horizon Europe SNS JU [DESIRE6G](https://desire6g.eu/) project, under grant agreement No.101096466, and the Spanish Ministry of Economic Affairs and Digital Transformation and the European Union-NextGenerationEU through the UNICO 5G I+D [6G-EDGEDT](https://unica6g.it.uc3m.es/6g-edgedt/) and 6G-[DATADRIVEN](https://unica6g.it.uc3m.es/6g-datadriven/).






