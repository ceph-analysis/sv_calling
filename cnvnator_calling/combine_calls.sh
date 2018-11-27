for output_dir in /uufs/chpc.utah.edu/common/home/u1072557/ceph_denovosv/calling/cnvnator_calling/results/*
do
    fam_vcf=$output_dir/$(echo $output_dir | awk -F/ '{print $NF}' ).vcf
    for cnv_file in $output_dir/*.cnvnator
    do
        sample_vcf="${cnv_file%.*}.vcf.gz"
        cnvnator2VCF.pl $cnv_file | bgzip > $sample_vcf
        tabix -p vcf $sample_vcf
    done
    bcftools merge $output_dir/*.vcf.gz -o $fam_vcf
done
