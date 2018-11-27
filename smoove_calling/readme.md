Downloaded binary from Brent repo
```
cd ~/bin
wget https://github.com/brentp/smoove/releases
```

## Got reference
```
cd ~/giab/ashkenazi_trio_dataset2/data/
wget --quiet http://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5.fa.gz
bgzip -fd hs37d5.fa.gz
samtools faidx hs37d5.fa
```
I stored this file in the data directory for GIAB for simplicity.

