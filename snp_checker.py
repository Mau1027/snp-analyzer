# snp_checker.py

# Sequenza wild-type di riferimento
wild_type = "AGATGCTTATAGATCGCGCTACATAGCTGATAGCTAG"

# Sequenze dei pazienti
sequenze_pazienti = {
    "paziente_1": "AGATGCTTATAGATCGCGCTACATAGCTGATAGCTAG",  # uguale
    "paziente_2": "AGATGCTTATAGATCGCGCTGCATAGCTGATAGCTAG",  # 1 SNP
    "paziente_3": "AGATGCTTATAGATCGTGCTGCATAGCTGATAGCTAG",  # 2 SNP
}

# Funzione per individuare SNP
def trova_snp(seq1, seq2):
    snps = []
    for i in range(min(len(seq1), len(seq2))):
        if seq1[i] != seq2[i]:
            snps.append((i, seq1[i], seq2[i]))
    return snps

# Analisi delle sequenze
for nome, seq in sequenze_pazienti.items():
    print(f"\nAnalisi di {nome}:")
    snps = trova_snp(wild_type, seq)
    if snps:
        print(f"  SNP trovati: {len(snps)}")
        for posizione, wt, mut in snps:
            print(f"    Posizione {posizione+1}: {wt} → {mut}")
    else:
        print("  Nessun SNP trovato (sequenza identica).")

    
