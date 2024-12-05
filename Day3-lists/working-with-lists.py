myList = ["Berlin", "Frankfurt", "Colonge", "Kahl", "Hamburg"]
print(myList)  # Print all the lists
print(len(myList))  # print the length

#  accessing with index numbers
print(myList[0])
print(myList[1])

print("Accessed from last: " + myList[-1])  # can be accessed from last


#  Range of Indexes
print("Accessed range: ")
print(myList[1:2])

if "Kahl" in myList:
    print("Included")

myList[2] = "Mainz"
print(myList)  # Print updated the lists
