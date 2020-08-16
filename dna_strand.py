# Function with one side of the DNA, you need to get the other complementary side. 
# DNA strand is never empty or there is no DNA at all.
def dna_strand(dna):
    dna = dna.replace("A", "1")
    dna = dna.replace("T", "2")
    dna = dna.replace("1", "T")
    dna = dna.replace("2", "A")
    
    dna = dna.replace("G", "1")
    dna = dna.replace("C", "2")
    dna = dna.replace("1", "C")
    dna = dna.replace("2", "G")
    
    return dna

Test.assert_equals(DNA_strand("AAAA"),"TTTT","String AAAA is")
Test.assert_equals(DNA_strand("ATTGC"),"TAACG","String ATTGC is")
Test.assert_equals(DNA_strand("GTAT"),"CATA","String GTAT is")