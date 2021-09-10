# This code reads a string and prints the number of times "A","C","G",and "T" appear

f = open("C:\\Users\\Brian Chau\\Downloads\\rosalind_dna.txt", "r")
dataset = f.readline()
print(dataset)
print(dataset.count("A"), dataset.count("C"), dataset.count("G"), dataset.count("T"))
f.close()