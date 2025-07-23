nextflow.enable.dsl=2

process GC_CONTENT {
    input:
    path fasta_file
    path script_file

    output:
    path "gc_output.txt"

    script:
    """
    python3 $script_file $fasta_file > gc_output.txt
    """
}

workflow {
    GC_CONTENT(
        file("chr22.fa"),
        file("bin/gc_content.py")
    )

    SNP_CHECKER(
        file("snp_sequences.fa"),
        file("bin/snp_checker.py")
    )
}

process SNP_CHECKER {
    input:
    path fasta_file
    path script_file

    output:
    path "snp_output.txt"

    script:
    """
    python3 $script_file $fasta_file > snp_output.txt
    """
}