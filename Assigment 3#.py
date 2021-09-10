file = open("C:\\Users\\Brian Chau\\Downloads\\rosalind_revc (1).txt", "r")
line = file.readline()[::-1]
file.close()

AnswerFile = open("C:\\Users\\Brian Chau\\Downloads\\answer_rosalind_revc.txt", "w+")
complement = {"A": "T", "T": "A", "G": "C", "C": "G", "\n": ""}
answer = ""
for x in line:
    answer += complement[x]
AnswerFile.write(answer)
AnswerFile.close()
