import pandas as pd
import json
import argparse
from pathlib import Path

def funannotate_gff_to_json(input_gff, output_json):
    """
    Convert Funannotate GFF file to a JSON file with correct column names according to GFF3 format.

    Parameters:
        input_gff (str): The path to the Funannotate GFF file.
        output_json (str): The path to the JSON file that will be created with the converted data.

    Returns:
        None

    This function reads a Funannotate GFF file, which is a tab-separated file containing genomic feature annotations
    for a genome assembly. The function converts the GFF data into a JSON format and saves it to a specified JSON file.

    The GFF file must have exactly 9 columns. The first seven columns represent the standard GFF fields, while the
    eighth column contains annotations in a semi-colon separated format.

    The resulting JSON file will have the following structure:
    {
        "seqid": "scaffold001",
        "source": "Funannotate",
        "type": "gene",
        "start": 1000,
        "end": 2000,
        "score": ".",
        "strand": "+",
        "phase": ".",
        "attributes": {
            "ID": "gene0001",
            "Name": "gene1",
            "Note": "example gene"
        }
    }
    """
    df = pd.read_csv(input_gff, sep="\t", skiprows=1, header=None)
    assert len(df.columns) == 9, f"Invalid column length: {df.columns}"

    container = {}

    for i in df.index:
        container[i] = {
            "seqid": df.loc[i, 0],
            "source": df.loc[i, 1],
            "type": df.loc[i, 2],
            "start": df.loc[i, 3],
            "end": df.loc[i, 4],
            "score": df.loc[i, 5],
            "strand": df.loc[i, 6],
            "phase": df.loc[i, 7],
        }

        annotation = df.loc[i, 8]
        annotation = annotation.split(";")
        container[i]["attributes"] = {}
        for item in annotation:
            if item == "":
                pass
            else:
                try:
                    k, v = item.split("=", 1)
                except ValueError as e:
                    print(item, e)
                container[i]["attributes"][k] = v

    Path(output_json).parent.mkdir(exist_ok=True, parents=True)
    pd.DataFrame.from_dict(container).to_json(output_json, indent=2)

def main():
    parser = argparse.ArgumentParser(description="Convert Funannotate GFF file to JSON format.")
    parser.add_argument("input_gff", help="Path to the Funannotate GFF file.")
    parser.add_argument("output_json", help="Path to the JSON file that will be created with the converted data.")
    args = parser.parse_args()

    funannotate_gff_to_json(args.input_gff, args.output_json)

if __name__ == "__main__":
    main()
