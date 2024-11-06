def amino_acid_percentages(protein,amino_acid_list=["A","I","L","M","F","W","Y","V"]):
    amino_acid_percentages=[]
    for amino_acid in amino_acid_list:
        count=0
        protein_length=len(protein)
        amino_acid_count=protein.count(amino_acid.upper())
        amino_acid_percentage=(amino_acid_count/protein_length)*100
        amino_acid_percentages.append(amino_acid_percentage)
    return sum(amino_acid_percentages)
        
assert round(amino_acid_percentages("MSRSLLLRFLLFLLLLPPLP", ["M"])) == 5
assert round(amino_acid_percentages("MSRSLLLRFLLFLLLLPPLP", ['F', 'S', 'L'])) == 70
assert round(amino_acid_percentages("MSRSLLLRFLLFLLLLPPLP")) == 65
        
