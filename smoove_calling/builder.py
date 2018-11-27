#! /usr/bin/env python
from __future__ import print_function
import sys
import os

PED="/uufs/chpc.utah.edu/common/home/u1072557/ceph_denovosv/data/16-08-06_WashU-Yandell-CEPH.ped"
OUTPUT="/uufs/chpc.utah.edu/common/home/u1072557/ceph_denovosv/ceph_scripts/cnvnator_calling/results/"
BAMDIR="/scratch/ucgd/lustre/ugpuser/Repository/AnalysisData/2016/A414/16-08-06_WashU-Yandell-CEPH/UGP/Data/PolishedBams/"
REF="/scratch/ucgd/lustre/ugpuser/ucgd_data/references/human_g1k_v37_decoy.fasta"

bams_by_fam = {}
fams = []
with open(PED, 'r') as pedfile:
    for line in pedfile:
        family_id,sample_id = line.strip().split()[:2]
        if family_id not in bams_by_fam:
            bams_by_fam[family_id] = []
        bams_by_fam[family_id].append(os.path.join(BAMDIR, sample_id + ".bam"))

for fam in bams_by_fam:
    if fam != "1353":
        continue
    command = "smoove call --duphold -x --name "+fam+" --fasta "+REF+" -p 4 --genotype "
    for bam in bams_by_fam[fam]:
        command += " " + bam
print(command)
