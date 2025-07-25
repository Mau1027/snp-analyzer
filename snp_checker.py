

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



    # Funzione per calcolare contenuto GC

# Sequenza wild type
WT = "AGATGCTTATAGATCGCGCTACATAGCTGATAGCTAG"

# Dizionario dei campioni paziente
pazienti = {
    "Paziente_1": "AGATGCTTATAGATCGCGCTACATAGCTGATAGCTAG",  # uguale al WT
    "Paziente_2": "AGATGCTTATAGATCGTGCCTACATAGCTGATAGCTAG",  # 2 SNP
    "Paziente_3": "AGATGCTTATAGATCGCGCTACATAGCTGATAGCTAC",  # 1 SNP
}

# Funzione per calcolare contenuto GC

def calcola_gc(seq):
    gc = seq.count("G") + seq.count("C")
    return round((gc / len(seq)) * 100, 2)

# Analisi per ogni paziente

for nome, seq in sequenze_pazienti.items():
    print(f"\nAnalisi di {nome}")
    
    snps = []  # lista per salvare gli SNP trovati
    for i in range(len(wild_type)):
        if i < len(seq) and seq[i] != wild_type[i]:
            snps.append((i+1, wild_type[i], seq[i]))  # posizione 1-based

for nome, seq in pazienti.items():
    print(f"\nAnalisi di {nome}")
    
    snps = []  # lista per salvare gli SNP trovati
    for i in range(len(WT)):
        if i < len(seq) and seq[i] != WT[i]:
            snps.append((i+1, WT[i], seq[i]))  # posizione 1-based


    if snps:
        print(f"  SNP trovati: {len(snps)}")
        for pos, ref, alt in snps:
            print(f"    Posizione {pos}: {ref} → {alt}")
    else:
        print("  Nessun SNP trovato.")

    gc_percent = calcola_gc(seq)

    print(f"  Contenuto GC: {gc_percent}%")

    print(f"  Contenuto GC: {gc_percent}%")

