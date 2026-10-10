#Dict
dict1 = {"name": "Abdullah" , "roll_no" : 686}
print(dict1)
dict1["name"] = "Ali"
print(dict1)
dict1.pop("roll_no")
print(dict1)

#Set
set1 = {1,2,3,4}
set2 = {3,4,5,6}
print(set1.union(set2))
print(set1.intersection(set2))

#List
list1 = [30,45,34,78,95]
print(list1)
list1.append(99)
print(list1)
list1.remove(45)
print(list1)
list1[3] = 100
print(list1)


#tuple
tup1 = (3.14,5.78,6)
print(tup1)