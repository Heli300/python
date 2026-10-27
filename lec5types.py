'''string functions'''
'''upper()	- Convert to uppercase'''
# name = "heli"
# print(name.upper())

'''lower() - Convert to lowercase'''
# name = "HELI"
# print(name.lower())

'''title() - First letter capital'''
# name = "hello wolrd!"
# print(name.title())

'''capitalize() -	Capitalize first character'''
# name = "HELLO wolrd!"
# print(name.capitalize())

'''strip() - Remove spaces'''
# text = "      program       "
# print(text.strip())

'''replace() -	Replace text'''
# text = "i like python"
# print(text.replace("python","java"))

'''split() - Convert string into list'''
# text = "i like python"
# print(text.split())

'''join() - Join list into string'''
# skills = ["python","java"]
# print(" ".join(skills))

'''find() - Find position'''
# text = "heli"
# print(text.find("l"))

'''count() - Count occurrences'''
# text = "python programming"
# print(text.count("m"))

'''startswith() - Check starting'''
# text = "heli"
# print(text.startswith("he"))

'''endswith() - Check ending'''
# text = "heli"
# print(text.endswith("p"))

'''isdigit() -	Check digits'''
# num= "heli"
# print(num.isdigit())

# num = "124"
# print(num.isdigit())

'''isalpha() -	Check alphabets'''
# num = "heli"
# print(num.isalpha())

# num = "124"
# print(num.isalpha())

'''list functions '''
'''append() - Add item'''
# name = ["heli","neel"]
# name.append("linsa")
# print(name)

'''extend() - Add multiple items'''
# numbers = [1,2]
# numbers.extend([3,4,5])
# print(numbers)

'''insert() - Insert at position'''
# name=["heli","neel"]
# name.insert(0,"linsa")
# print(name)

'''remove() - Remove item'''
# name=["heli","neel"]
# name.remove("heli")
# print(name)

'''pop() - Remove by index'''
# numbers = [1,2,3,4,5,6]
# numbers.pop(2)
# print(numbers)

'''clear() - Remove all items'''
# numbers = [1,2]
# numbers.clear()
# print(numbers)

'''index()	- Find position'''
# name =["heli","neel"]
# print(name.index("heli"))

'''count()	- Count values'''
# numbers = [1,1,2,3,4,5]
# print(numbers.count(1))

'''sort() - Sort list'''
# numbers = [1,4,5,6,7,2,8,1]
# numbers.sort()
# print(numbers)

'''reverse() - Reverse list'''
# numbers = [1,2,3]
# numbers.reverse()
# print(numbers)

'''copy() - Copy list'''
# a = [1,2,3]
# b = a.copy()
# print(b)

'''tuple methods'''
'''count() - Count values'''
# data = (1,1,2,3)
# print(data.count(1))

'''index() - Find position'''
# data = (1,1,2,3)
# print(data.index(2))

'''set methods'''
'''add() - Add item'''
# numbers = {1,2,3}
# numbers.add(4)
# print(numbers)

'''update() - Add multiple items'''
# numbers.update([5,6])
# print(numbers)

'''remove() - Remove item'''
# numbers = {10,20,30}
# numbers.remove(10)

'''discard() - Remove safely'''
# numbers = {10,20,30}
# numbers.discard(10)

'''union() - Combine sets'''
# a = {1,2}
# b = {2,3}
# print(a.union(b))

'''intersection() - Common values'''
# print(a.intersection(b))

'''pop() - Remove random item'''
# numbers = [1,2,3,4,5,6]
# numbers.pop(2)
# print(numbers)

'''clear() - Remove all'''
# numbers = [1,2]
# numbers.clear()
# print(numbers)

'''difference() - Unique values'''
# A = {10, 20, 30, 40}
# B = {30, 40, 50, 60}
# print(A.difference(B))

'''Dictionary Methods (dict)'''
'''keys() - Get keys'''
# student = {
#     "name": "Rahul",
#     "age": 21
# }
# print(student.keys())

'''values() - Get values'''
# student = {
#     "name": "Rahul",
#     "age": 21
# }
# print(student.values())

'''items() - Get key-value pairs'''
# student = {
#     "name": "Rahul",
#     "age": 21
# }
# print(student.items())

'''get() - Get value safely'''
# student = {
#     "name": "Rahul",
#     "age": 21
# }
# print(student.get("name"))

'''update() - Update dictionary'''
# student = {
#     "name": "Rahul",
#     "age": 21
# }
# student.update({"city":"Ahmedabad"})
# print(student)

'''pop() - Remove item'''
# student = {
#     "name": "Rahul",
#     "age": 21
# }
# student.pop("age")
# print(student)

'''clear() - Remove all'''
# numbers = [1,2]
# numbers.clear()
# print(numbers)

'''copy() - Copy dictionary'''
# a = [1,2,3]
# b = a.copy()
# print(b)