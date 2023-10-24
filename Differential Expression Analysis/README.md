# Differential Expression Analysis README

**Author:** nithyasarabudla  
**Date:** 19/02/2023

## Overview

This README provides an overview of the methodology and results for a Differential Expression Analysis project. The project focuses on identifying differentially expressed genes using RNA-Seq data and includes the following key steps and scripts:

## Methods

### Estimating Relative Abundance

- Salmon (Patro et al. 2017) is used to estimate relative transcript abundance.
- tximport (Soneson, Love, and Robinson 2016) is used to import Salmon abundance estimates.
- DESeq2 (Love, Huber, and Anders 2014) is employed to perform statistical tests for identifying differentially expressed genes.

### Scripts

- **buildIndex.sh:** Builds a Salmon index from a de-novo transcriptome with a k-mer length of 25.

- **alignAll.sh:** Performs Salmon abundance estimation for all samples, generating an output directory named "quant."

- **mergeKo.R:**
  - Combines data from transcriptBlast.txt, kegg.txt, and ko.txt to create the tx2gene table, mapping transcripts to genes.
  - Filters BLAST hits, ensuring they cover at least 50% of the target sequence.
  - Produces a final tx2gene.csv file containing transcript to KO mappings.

- **de.R:**
  - Imports quant.sf files for each sample using tximport().
  - Creates a DESeqDataSet and performs differential expression analysis using DESeq2.
  - Filters results with an adjusted p-value less than 0.05.
  - Annotates gene IDs with pathways and descriptions, saving the results in deAnnotated.csv.

## Results

Sample differential expression results:
"ko","pathway","description","log2FoldChange","padj","Factor"
"ko:K17920","path:ko04144","Endocytosis",0.8755,0.0035,"Menthol_Menthol_vs_Control"
