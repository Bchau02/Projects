# This code reads in a text file containing a dna string
# and transcribes it into an rna string by switching out "T" for "U"

file = open("C:\\Users\\Brian Chau\\Downloads\\rosalind_rna.txt", "r+")
DnaString = file.readline()
file.close()
AnswerFile = open("C:\\Users\\Brian Chau\\Downloads\\rosalind_rna_answer.txt", "w+")
answer = AnswerFile.write(DnaString.replace("T", "U"))
AnswerFile.close()
