def amino_acid_percentages(protein,amino_acid):
    protein_length=len(protein)
    amino_acid_count=protein.count(amino_acid.upper())
    amino_acid_percentage=(amino_acid_count/protein_length)*100
    return amino_acid_percentage

assert round(amino_acid_percentages("MSRSLLLRFLLFLLLLPPLP", "M")) == round(5)
assert round(amino_acid_percentages("MSRSLLLRFLLFLLLLPPLP", "r")) == round(10)
assert round(amino_acid_percentages("MSRSLLLRFLLFLLLLPPLP", "L")) == round(50)
assert round(amino_acid_percentages("MSRSLLLRFLLFLLLLPPLP", "Y")) == round(0)