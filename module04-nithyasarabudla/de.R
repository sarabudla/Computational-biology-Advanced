#!/usr/bin/env Rscript
# de.R
library(tximport)
library(readr)
library(DESeq2)
library(dplyr)
library(tibble)
library(knitr)
# Define constants
TESTING <- FALSE # Change to FALSE if using entire Samples set
RESULTS_DIR <- "/home/sarabudla.n/BINF6309/module04-nithyasarabudla/scripts"
AIPTASIA_DIR <- "/work/courses/BINF6309/AiptasiaMiSeq"

# for testing purposes - alternative samples table
testing_samples <- data.frame(Sample = c("Aip02", "Aip02", "Aip02", "Aip02"),
                              Menthol = c("Control", "Control", "Menthol", "Menthol"),
                              Vibrio = c("Control", "Vibrio", "Control", "Vibrio"))
head(testing_samples)

# True script begins
tx2gene <- read.csv(file.path(RESULTS_DIR, "tx2gene.csv"))
head(tx2gene)

if (TESTING) {
  print("*Running test with Aip02 only*")
  samples <- testing_samples
} else {
  samples <- read.csv(file.path(AIPTASIA_DIR, "Samples.csv"), header=TRUE)
}
head(samples)

tx2gene <- read.csv(file.path(RESULTS_DIR, "tx2gene.csv"))
files <- file.path(RESULTS_DIR, "quant", samples$Sample, "quant.sf")
txi <- tximport(files, type="salmon", tx2gene=tx2gene)
dds <- DESeqDataSetFromTximport(txi, colData = samples, 
                                design = ~Menthol + Vibrio)


dds$Vibrio <- relevel(dds$Vibrio, ref = "Control")
dds$Menthol <- relevel(dds$Menthol, ref = "Control")
keep <- rowSums(counts(dds)) >= 10
dds <- dds[keep,]
dds <- DESeq(dds)

padj <- .05
minLog2FoldChange <- .5
dfAll <- data.frame()
# Get all DE results except Intercept, and "flatten" into a single file.
for (result in resultsNames(dds)){
  if(result != 'Intercept'){
    res <- results(dds, alpha=.05, name=result)
    dfRes <- as.data.frame(res)
    dfRes <- subset(subset(dfRes, select=c(log2FoldChange, padj)))
    dfRes$Factor <- result
    dfAll <- rbind(dfAll, dfRes)
  }
}
head(dfAll)

write.csv(dfAll, file=file.path(RESULTS_DIR, "dfAll.csv"))


# filter for adjusted p-value < 0.05

de <- subset(dfAll, padj < 0.05)
row.names(de)<-c('ko:K13785', 'ko:K14965', 'ko:K17920',
                 'ko:K006431', 'ko:K012061', 'ko:K012511', 
                 'ko:K015961', 'ko:K016811', 'ko:K021831', 
                 'ko:K028721', 'ko:K028731', 'ko:K028771',
                 'ko:K029801', 'ko:K030071', 'ko:K036261', 
                 'ko:K057541', 'ko:K089571', 'ko:K095691', 
                 'ko:K107041', 'ko:K137581','ko:K147531',
                 'ko:K150251', 'ko:K161861', 'ko:K197651', 'ko:K203691')
de<-rownames_to_column(de,var="ko")
loc <- read.delim("/home/sarabudla.n/BINF6309/module04-nithyasarabudla/scripts/path.txt", header = FALSE, stringsAsFactors = FALSE)
colnames(loc) <- c("ko", "pathway")
loc_name <- read.delim("/home/sarabudla.n/BINF6309/module04-nithyasarabudla/scripts/ko", header = FALSE, stringsAsFactors = FALSE)
colnames(loc_name) <- c("pathway", "description")
new <- merge(loc, loc_name, by="pathway", all.y=TRUE)
de_annotated <- merge(de, new, by="ko") %>% select(ko, pathway, description, log2FoldChange, padj, Factor) 
write.csv(de_annotated, file=file.path(RESULTS_DIR, "deAnnotated.csv"),row.names = FALSE)
#write.csv(de_annotated, file = "deAnnotated.csv", row.names = FALSE)
kable(de_annotated)
# end of de.R script