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

# Adding list items
additems = ["Berlin", "Frankfurt", "Colonge", "Kahl", "Hamburg"]
additems.append("hanau")  # will add to last
print(additems)

additems.insert(3, "Bonn")  # specific index add item
print(additems)

#  Extend List
#  To append elements from another list to the current list, use the extend() method.

newList1 = ["a", "b", "c"]
newList2 = ["x", "z", "z"]

newList2.extend(newList1)
print(newList2)

# can extend any interative object
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

# Remove from list
thislist.remove("cherry")
newList2.pop(2)
del thislist[1]

print(f"after REMOVE: ")
print(thislist)
print("After POP: ")
print(newList2)
print("After DEL:")
print(thislist)

print("==================\n Working with loops \n==============")

print("normal list print")
for x in additems:
    print(x)
print("Printing with index number")
for x in range(len(additems) - 1, -1, -1):
    print(additems[x])

print("short hand print")
[print(x) for x in additems]
