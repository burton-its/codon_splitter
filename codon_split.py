gene = "GGCTAGCTAATCGCT" 

#while loop to split nucleotide sequence into codons
# i = 0
# while i <= len(gene):
# 	codon = gene[i:i+3]
# 	i+=3
# 	print(codon)



#list comprehension to do the same thing
codon = [gene[i:i+3] for i in range(0,len(gene),3)]
print(codon)
