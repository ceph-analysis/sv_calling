#! /usr/bin/env python
from __future__ import print_function
import sys
import os
import pysam
import fnmatch

PED="/uufs/chpc.utah.edu/common/home/u1072557/ceph_denovosv/data/16-08-06_WashU-Yandell-CEPH.ped"
ANALYSIS_PATH="/uufs/chpc.utah.edu/common/home/u1072557/ceph_denovosv/calling/manta_calling/results"
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

regions = range(1,23)
regions = [str(x) for x in regions] + ['Y','X']
regions = ["--region " + x for x in regions]

for fam in bams_by_fam:
    print (fam)
    command = "configManta.py"
    for bam in bams_by_fam[fam]:
        command += " --bam " + bam
    command += " --referenceFasta " + REF
    command += " " + " ".join(regions)
    command += " --runDir "  + os.path.join(ANALYSIS_PATH,fam)
    print(command)
