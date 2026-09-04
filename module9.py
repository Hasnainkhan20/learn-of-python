# modle 9
# topic name = Dictionary
# coding exercise

# q1
# fruites_prices = {"Strawberry" : 15, "Grapes" : 20, "Pineapple" : 30}
# fruites_prices["Grapes"] = 25 #update q2
# fruites_prices["banana"] = 10 #add q2
# print(fruites_prices.get("apple")) #get q3
# print(fruites_prices.keys()) #keys q4
# print(fruites_prices.values()) #values q4
# for Fruits in fruites_prices: # for loop use q5
#  print(fruites_prices.items())
#  for keys , values in fruites_prices.items():
#   print(f"{keys} -> {values}")
# fruites_prices.update({"apple" : 20, "cheery" : 25, "Grapes" : 40} )
# print(fruites_prices)
# value_delet = fruites_prices.pop("Pineapple")
# print(fruites_prices)
# print(value_delet) #.pop use q6
# students = {
#     "student1" : {"name" : "ahsan", "age" : 19},
#     "student2" : {"name" : "ali", "age" : 18},
# }
# print(students["student1"]["name"])
# print(students["student2"]["name"]) #nested dictionary q7
# fruites_name = {"watermelon" : 15, "apple" : 20, "cheery" : 30}
# fruites_name.clear()
# print(fruites_name)  #.clear use q8
# print(fruites_prices)



# debuging exercise
# debug1
# student = {"name" = "Ali", "age": 20} 
# print(student) 
# student = {"name": "Ali", "age": 20}
# print(student) 


# debug2
# student = {"name": "Ali"} 
# print(student["age"]) 
# student = {"name": "Ali"} 
# print(student.get("age")) 


# debug3
# student = {"name": "Ali", "age": 20} 
# keys = student.keys() 
# print(keys[0]) 
# student = {"name": "Ali", "age": 20} 
# keys = student.keys()
# print(keys)  


# debug4
# student = {} 
# item = student.popitem()  
# student = {"name" : "ayesha", "class" : 7} 
# item = student.popitem() 
# print(item)


# debug5
# student = {"name": "Ali", "age": 20} 
# for k in student.values():     
#     print(k, student[k]) 
# student = {"name": "Ali", "age": 20} 
# for k in student.values():    
#      print(k, student) 


#mini assignment
# employee dictionary
# employee = {"name" : "ali", "department" : "finance", "salary" : 25000}
# print(f"employee_dictionary: {employee}")
# bonus_value = employee.get("bonus",0)
# print(f"bonus_value:{bonus_value}")
# employee.update({"salary" : 30000, "experience" : "2years" })
# print(f"dictionary after updation:{employee}")
# for keys , values in employee.items():
#   print(f"{keys} : {values}")
# remove_field = employee.pop("department")
# print(f"deleted item: {remove_field}")
# print(f"final dictionar:{employee}")


# miniproject
students = {
    "rollno1" : {"name" : "ahsan", "age" : 19, "marks": 65},
    "rollno2" : {"name" : "ali", "age" : 18, "marks" : 70},
    "rollno3" : {"name" : "hashir", "age" : 20, "marks" : 75},
}
print(students["rollno1"]["name"]["age"]["marks"])
print(students["rollno2"]["name"]["age"]["marks"])
print(students["rollno3"]["name"]["age"]["marks"])

user_name = input("enter your name ")
user_age = int(input("enter your age "))
user_rollno = int(input("enter your rollnum "))
user_marks = int(input("enter your marks "))

students.update({
    "name1" :{"name" : "user_name", "user_age" : "age2", "rollno" : "user_rollno", "marks" : "user_marks"}
    })
search_rollno = input("enter your search_rollno")
if search_rollno == None:
    print("record not found ")
else:
    print()














# books_names = {"book1" : "english", "book2" : "urdu", "book3" : "science", "book4" : "math"}
# games_names = {"game1" : "cricket", "game2" : "football", "game3" : "hockey", "game4" : "basketball"}
# print(games_names["game2"])
