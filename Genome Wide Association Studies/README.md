# PLINK Analysis 

This provides an overview of the PLINK analysis performed on a dataset consisting of randomly chosen genotypes from 89 Asian HapMap subjects. The analysis includes various steps such as data preparation, quality control, stratification, association testing, and results interpretation.

## Data Preparation

- The dataset used in this analysis consists of approximately 80,000 autosomal SNPs.
- The root name of the input files is provided to PLINK using the `--file` option.
- By default, PLINK expects a `.ped` file for genotype information and a `.map` file for marker information in the current working directory.
- However, the `--ped` and `--map` options can be used to specify different file locations and names.
- The dataset was examined for missing values, and individuals and SNPs were removed based on predetermined criteria.

## Creating Binary PED File

- To save storage space and expedite analysis, a binary PED file was created using the `--make-bed` option.
- The `--mind`, `--geno`, and `--maf` options can be used to manually specify filters for missing rate and allele frequency.
- The resulting files include `hapmap1.bed`, `hapmap1.bim`, and `hapmap1.fam`.

## Working with the Binary PED File

- The `--bfile` option was used to specify the input data in binary format.
- This resulted in faster data loading and eliminated the need for `.ped` and `.map` files.

## Summary Statistics: Missing Rates

- The `--missing` option was used to generate summary statistics on the percentage of missing data.
- The results are saved in two files, `miss_stat.imiss` (per individual) and `miss_stat.lmiss` (per SNP).

## Summary Statistics: Allele Frequencies

- The `--freq` option was used to calculate allele frequencies for each SNP.
- The output is saved in the `freq_stat.frq` file.
- A stratified analysis was performed using the `--within` option and a cluster variable.

## Basic Association Analysis

- Simple association analysis was performed for the disease trait using the `--assoc` option.
- The results include a list of SNPs, chi-squared statistics, and significance values.

## Stratification Analysis

- Individuals were stratified based on genetic identity using the `--cluster` option.
- Cluster analysis helped reduce false positive rates and improve the precision of association analysis.
- Various methods were demonstrated for clustering, including simple IBS-based clustering, restriction-based clustering, and external clustering.

## Quantitative Trait Association Analysis

- Quantitative trait association analysis was performed using the `--assoc` option.
- Ordinary least squares regression was used to analyze the quantitative trait.
- Empirical p-values were calculated to account for multiple testing.

## SNP Extraction

- A specific SNP or group of SNPs can be extracted from the dataset using the `--recode` option.
- In this example, the `--recodeAD` option was used to create a file with genotypes coded for additive and dominance components.

## Additional Analyses

- The extracted data can be imported into other statistical software for further analysis.
- For example, logistic regression was demonstrated in R using the imported data.

## Summary

- PLINK provides a powerful tool for genetic data analysis, including quality control, association testing, and data extraction.
- The choice of analysis methods and strategies depends on the research objectives and characteristics of the dataset.


