file=open("Rosalind Files//rosalind_iprb.txt", "r")


raw_string=file.read()
file.close()

splits=raw_string.split()
k=int (splits[0])
m= int (splits[1])
n= int (splits[2])
sum=k+m+n

answer=1-((n/sum)*(n-1)/(sum-1)+1/2*(n/sum)*(m/(sum-1))+(m/sum)*(n/(sum-1))*1/2+1/4*(m/sum)*(m-1)/(sum-1))
print(answer)