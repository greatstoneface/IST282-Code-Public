name1 = "Kevin Snow"
name2 = "kevin snow"

print (name1[3])

if name1 == name2:
    print("same")
else:
    print("not same")


if name1.islower():
    print("True")
else:
    print("False")

if name2.islower():
    print("True")
else:
    print("False")


upperNum = 0 #initial value
for ch in name1:   #name1 = "Kevin Snow"
    print(ch)
    if ch.isupper():
        upperNum = upperNum + 1
        
print(upperNum)


# print all the elements in the string name1
index = 0
upperNum = 0
while (index < len(name1)):
    print(name1[index])
    if name1[index].isupper():
        upperNum = upperNum + 1
    index = index + 1

print(upperNum)

    

