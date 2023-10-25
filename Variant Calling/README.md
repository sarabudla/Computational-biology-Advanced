# Genomic Variant Calling Pipeline

This repository contains scripts and instructions for running a genomic variant calling pipeline, focusing on identifying genomic differences between individuals (germline) and within tissues of a single individual (somatic). The pipeline is based on the Genome Analysis Tool Kit (GATK) and DeepVariant for variant calling.

## Methods

Detailed information on the methods used in this pipeline can be found in the main document.

## Repository Contents

- `getGenome.sh`: Script for retrieving the GRCh38 reference genome from the Gencode FTP server.
- `getReads.sh`: Script for retrieving NGS reads from the SRA under accession SRR6808334.
- `trimReads.sh`: Script for quality trimming the reads using Trimmomatic.
- `indexGenome.sh`: Script for indexing the genome for use by BWA.
- `alignReads.sh`: Script for aligning the reads using BWA mem.
- `sort.sh`: Script for sorting the file created by BWA mem to a sorted BAM.
- `indexReads.sh`: Script for indexing the reads.
- `runDeepVariant.sh`: Script for producing a VCF file using DeepVariant.
