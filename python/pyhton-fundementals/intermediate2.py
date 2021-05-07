# 1
# x = [ [5,2,3], [10,8,9] ] 
# students = [
#     {'first_name':  'Michael', 'last_name' : 'Jordan'},
#     {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 20} ]
# x[1][0]=15
# print(x)
# students[1]["first_name"]="Braynt"
# print(students)
# sports_directory["soccer"][0]="Andres"
# print(sports_directory)
# z[0]["y"]=30
# print(z)

# 2
# students = [
#         {'first_name':  'Michael', 'last_name' : 'Jordan'},
#         {'first_name' : 'John', 'last_name' : 'Rosales'},
#         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#         {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ]
# def iterateDictionary(students): 
#     for i in range(0,len(students)):
#         print("first name : ",students[i]["first_name"],",  last name : " ,students[i]["last_name"])
# iterateDictionary(students)

# 3
# students = [
#         {'first_name':  'Michael', 'last_name' : 'Jordan'},
#         {'first_name' : 'John', 'last_name' : 'Rosales'},
#         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#         {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ]
# def iterateDictionary(key,students): 
#     for i in range(0,len(students)):
#         print(f"{key} : ",students[i][key])
# iterateDictionary("first_name",students)
# iterateDictionary("last_name",students)

# 4
# dojo = {
#     'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
#     'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
# }
# def printInfo(dojo):
#     print(len(dojo["locations"]),"locations")
#     for i in range(len(dojo["locations"])):
#         print(dojo["locations"][i])
#     print(len(dojo["instructors"]),"instructors")
#     for j in range(len(dojo["instructors"])):
#         print(dojo["instructors"][j])
# printInfo(dojo)
