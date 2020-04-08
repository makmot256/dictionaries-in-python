
student = {'name': "john", 'age': 25, 'courses': [maths, compsi]}
print(student['name'])
print(student['courses'])

student = {1: "john", 'age': 25, 'courses': [maths, compsi]}

print(student[1])
print(student.items())

# prints out only the keys of the dictionary
print(student.keys())

# prints out only the values of the dictionary
print(student.values())

for keys in student:
 print(keys)

for values in student:
    print(values)

# prints both the keys and values in the dictionary
for key, value in student.items
  print(key, value)

# prints out none of the keys that exists within the dictionary
  print(student.get('none'))

# prints out none of the keys that exists within the dictionary
  print(student.get('none'))
  print(student.get('phone' , 'not found'))

# to update anything within the dictionary
  print(student.update({'name': 'Jane', 'Age':30, 'courses':[software,information tech]}))
  
# to delete the value in the dictionary
  print(student.del())
  
  
print(student.values())
print(student.keys())






















































































