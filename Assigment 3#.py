# This code reads in a dna string and writes the reverse complement to another txt file
file = open("C:\\Users\\Brian Chau\\Downloads\\rosalind_revc (1).txt", "r")
# line reads the first line of the file and reverses it by using a slice
line = file.readline()[::-1]
file.close()

AnswerFile = open("C:\\Users\\Brian Chau\\Downloads\\answer_rosalind_revc.txt", "w+")
# complement is a dictionary coding in the appropriate base conversions
complement = {"A": "T", "T": "A", "G": "C", "C": "G", "\n": ""}
answer = ""
for x in line:
    answer += complement[x]
AnswerFile.write(answer)
AnswerFile.close()
