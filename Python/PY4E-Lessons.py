#I am going to use this file for the Py4E lesson
found = False
print("Before", found)
for value in [9,41,12,3,74,15,34,56,85] :
    if value == 3 :
        found = True
        break
    print(found, value)
print("After",found,value)
