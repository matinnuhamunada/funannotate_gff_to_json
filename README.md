## A quick script for converting GFF3 to json and vice versa
This script was meant for a quick exploration of gff3 file for Mas Luthfi.

### Clone the repository
```bash
git clone https://github.com/matinnuhamunada/funannotate_gff_to_json.git
cd funannotate_gff_to_json.
```

### Create the conda environment
Using conda or mamba to create the python environment

```bash
conda env create -f env.yaml 
```

### Activate the environment
```bash
conda activate gff_utils 
```

### Convert gff to json
```bash
python scripts/funannotate_gff_to_json.py <myfile.gff> <output.json>
```

### Manipulate json with Jupyter notebook
Activate jupyter notebook
```bash
jupyter lab
```

Navigate to the example notebook in `notebooks/Example.ipynb`

### Convert json back to gff
```bash
python scripts/funannotate_json_to_gff.py <myfile.json> <output.gff> 
```
