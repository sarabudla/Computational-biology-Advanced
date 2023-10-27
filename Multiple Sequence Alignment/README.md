# Bioinformatics Pipeline README

## Overview
This repository contains a set of scripts and programs for conducting bioinformatics analyses. These tools are designed to align DNA or RNA sequences, translate RNA sequences to amino acids, and facilitate sequence alignment using ClustalO.

## Prerequisites
Before using the scripts and programs in this repository, you will need to have the following software and modules installed on your system:

- ClustalO
- Anaconda3
- BioPython

## Usage

### `clustalAlign.sh`

This shell script is used to perform sequence alignment using ClustalO.

- Usage:
  - Copy `clustalAlign.sh` to your working directory.
  - Modify the input file path in the script to specify the location of your input FASTA file.
  - Run the script using the command: `sbatch sbatch_clustalAlign.sh /path/to/working_directory`

### `sbatch_clustalAlign.sh`

This Slurm batch script is used to submit the ClustalO alignment job to a computing cluster. It ensures the alignment script is executed with the necessary resources.

- Usage:
  - Copy `sbatch_clustalAlign.sh` and `clustalAlign.sh` to your working directory.
  - Run the script using the command: `sbatch sbatch_clustalAlign.sh /path/to/working_directory`

### `translate_APOE.py`

This Python script translates RNA sequences to amino acids. It uses the BioPython library to perform the translation.

- Usage:
  - Place the input RNA sequences in a FASTA file (e.g., `APOE_refseq_transcript.fasta`).
  - Update the input and output file paths in the script.
  - Run the script using the command: `python translate_APOE.py`

## Output

- `clustalAlign.sh` will produce an aligned sequence file named `apoe_alignment.fasta`.
- `translate_APOE.py` will create an amino acid sequence file named `apoe_aa.fasta`.



