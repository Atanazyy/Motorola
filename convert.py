def decode(rna):
    table = {'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    } #map from geeksforgeeks
    allnuc = ['A', 'T', 'G', 'C']

    res = set()
    rna = rna.upper()
    rna = list(rna)
    n = len(rna)
    if('U' in rna and 'T' in rna):
        print("sekwencja zawiera jednoczesnie U i T") 
        return -1
    for i in range(n):
        nuc = rna[i]
        if(nuc == 'U'):
            rna[i] = 'T'
        if(not rna[i] in allnuc):
            print("sekwencja zawiera inne litery niz A, T, U, G, C") 
            return -1
        
    for start in range(3):
        prot = ""
        for i in range(start, n, 3):
            if(i + 3 > n):
                break
            cod = rna[i : i + 3]
            cod = cod[0] + cod[1] + cod[2]
            ami = table[cod]
            if(ami == 'M' and len(prot) == 0):
                prot += ami
            elif(ami == "_" and len(prot) > 0):
                res.add(prot)
                prot = ""
            elif(len(prot) > 0):
                prot += ami
    return res
