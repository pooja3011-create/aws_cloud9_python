# -*- coding: utf-8 -*-

"""
TODO: add docstring
"""
import logging
import re
import json

# name of the file to be read
fname = "preproinsulin-seq.txt"
structure_fname = "insulin_structure.json"
file_suffix = "-seq-clean.txt"
amino_acid_weights_fname = "amino_acid_weights.json"

# logging information
FORMAT = '%(levelname)-8s | %(message)s'
logging.basicConfig(format=FORMAT, level=logging.DEBUG)

pattern = r"^[0-9]*([a-z\s]*)$"

# lists to contain the information
clean_lines = list()
sequences = list()


# get the insulin structure. Array of objects
# - name: string, name of the section, becomes the file prefix
# - start: int, starting index in the sequence (1-based)
# - end: int, ending index in the sequence (1-based)
with open(structure_fname, "rt") as sfile:
    insulin_structure = json.load(sfile)


# read the amino acid weights
# - "<char>" : weight
# - character : float
with open(amino_acid_weights_fname, "rt") as aa_weights_file:
    amino_acid_weights = json.load(aa_weights_file)


# parse the insulin file
with open(fname, "rt") as insulin_file:
    for line_number, line in enumerate(insulin_file):
        logging.debug(f"::: working on line {line_number}")
        
        # remove the whitespace
        line = line.strip()
        
        # exclude the non-data part
        if line.startswith("ORIGIN"):
            logging.debug("ORIGIN line is found. Excluding it from the clean data")
            continue
        
        if line.startswith("//"):
            logging.debug("// line is found. Excluding it from the clean data")
            continue
    
        # parse the data
        match = re.match(pattern, line)
        if match is  None:
            logging.error(f"Could not find a regex on line {line_number}")
            continue
    
        # extract the match
        logging.debug(f"::: Parsed the following sequence on line: {line_number}")
        parsed_sequence = match.groups()[0].strip()
        logging.debug(parsed_sequence)
        
        # save the parsed sequence
        current_sequences = parsed_sequence.split(" ")
        sequences.extend(current_sequences)

logging.info(f"Finished processing the file {fname}")

# merge everthing into a single string
sequence_string = "".join(sequences)

# sanity check
assert len(sequence_string) == 110
logging.info("Successfully parsed the DNA sequence")

logging.debug(sequences)
logging.debug(sequence_string)

# post processing
for section in insulin_structure:
    name = section["name"]
    start = int(section["start"])-1
    end = int(section["end"])-1
    subsection = sequence_string[start : end+1]

    out_fname = f"{name}{file_suffix}"
    with open(out_fname, "wt") as out_file:
        out_file.write(subsection)
    logging.info(f"wrote {len(subsection)} characters to the file: {out_fname}")
    logging.debug(subsection)

amino_acid_counts = dict()

sorted(set(sequence_string))

breakpoint()