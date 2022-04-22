
# file=open('sample.txt',"r")     #Q-1
# for line in file.readlines():
#     lst=line.split()
#     for element in lst:
#         if element=='':
#             lst.remove(element)
#     open('sample1.txt',"a").write(' '.join(lst)+"\n")

# file.close()
    

# for line in open('sports.dat',"r").readlines(): #Q-2
#     if line.split("~")[0]=='Atheletics':
#         open('Atheletics.dat',"a").write(line)


# file=open('telephone.txt',"r")  #Q-3
# data=file.readlines()
# print("-"*27)
# for line in data:
#     rec=line.split()
#     print("| {:<13s} | {:>7s} |".format(rec[0],rec[1]))
#     print("-"*27)
# file.close()


# file=open("Poem.txt","r")  #Q-4
# data=file.readlines()
# count1,count2=0,0

# for line in data:
#     rec=line.split()
#     for word in rec:
#         if word in ("The","the"):
#             count1+=1
#         elif word in ("To","to"):
#             count2+=1

# print("Word 'the' appears",count1,"times.")
# print("Word 'to' appears",count2,"times.")
# file.close()

