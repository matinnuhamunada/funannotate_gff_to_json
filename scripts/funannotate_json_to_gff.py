import pandas as pd
import json
import argparse

def funannotate_json_to_gff(input_json, output_gff):
    """
    Convert Funannotate JSON file to a GFF file with correct GFF3 format.

    Parameters:
        input_json (str): The path to the Funannotate JSON file.
        output_gff (str): The path to the GFF file that will be created with the converted data.

    Returns:
        None

    This function reads a Funannotate JSON file, which was previously generated from the GFF data using the
    funannotate_gff_to_dict function. The function converts the JSON data back to the original GFF3 format and
    saves it to a specified GFF file.

    The JSON file should have the following structure:
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
    with open(input_json, "r") as json_file:
        data = json.load(json_file)

    gff_lines = []

    for i, entry in data.items():
        attributes = []
        for key, value in entry["attributes"].items():
            attributes.append(f"{key}={value}")
        attributes_str = ";".join(attributes)

        gff_line = "\t".join([
            entry.get("seqid", ""),
            entry.get("source", ""),
            entry.get("type", ""),
            str(entry.get("start", "")),
            str(entry.get("end", "")),
            entry.get("score", ""),
            entry.get("strand", ""),
            entry.get("phase", ""),
            attributes_str
        ])
        gff_lines.append(gff_line)

    with open(output_gff, "w") as gff_file:
        gff_file.write("#gff-version 3\n")
        gff_file.write("\n".join(gff_lines))

def main():
    parser = argparse.ArgumentParser(description="Convert Funannotate JSON file to GFF format.")
    parser.add_argument("input_json", help="Path to the Funannotate JSON file.")
    parser.add_argument("output_gff", help="Path to the GFF file that will be created with the converted data.")
    args = parser.parse_args()

    funannotate_json_to_gff(args.input_json, args.output_gff)

if __name__ == "__main__":
    main()
