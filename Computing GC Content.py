file = open("C://Users//Brian Chau//Downloads//rosalind_gc.txt", "r")


def percentage_gc(string):
    count = 0
    for x in string:
        if (x == "G" or x == "C"):
            count += 1

    return count * 100 / (len(string))


raw_string = file.read()
file.close()

raw_string_nnl = raw_string.replace("\n", "")


splits = raw_string_nnl.split(">")
splits.pop(0)

gc_tracker = percentage_gc(splits[0][13:])

for index in range(len(splits)):
    if percentage_gc(splits[index][13:]) > gc_tracker:
        gc_tracker = percentage_gc(splits[index][13:])
        marker = index

answer_file = open("C://Users//Brian Chau//Downloads//rosalind_gc_answer.txt", "w")
answer_file.write(splits[marker][:13])
answer_file.write("\n")
answer_file.write(str(gc_tracker))
answer_file.close()

