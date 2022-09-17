file = open("Rosalind Files//rosalind_hamm.txt","r")

raw_string=file.read()
file.close()

marker=0;

for x in range(len(raw_string)):
    if(raw_string[x]=="\n"):
        marker =x
        break

split=raw_string.split()
first_string = split[0]
second_string = split[1]
# first_string=raw_string[0:marker]
# second_string=raw_string[marker+1:]

count=0;

for x in range(len(first_string)):
    if first_string[x]!= second_string[x]:
        count=count+1

print(count);
