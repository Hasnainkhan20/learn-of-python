# function module
# coding exercise
# q1
# def average(num1, num2):
#     return (num1 + num2) /2


# print(average(40 , 35))



# q2
# def result(a=1 , b=2):
#     print(a+b)

# result()


# q3
# def maximum(*value):
#     maxnumber = max(value)
#     print(maxnumber)

# maximum(50, 30, 90, 60, 10)


# # q4
# def student_info(**details):
#     print(details)

# student_info(name = "hasnain" , age = 17 , city = "karachi")



# q5
# cube = lambda a: a**3
# print(cube(5))



# q6
# def sum_number(number):
#     if number == 16:
#      return
#     numbers += sum_number
#     print(sum_number)

# sum_number(+1)




# q7 
# counter = 10
# def update_counter ():
#    global counter
#    counter +=1
# update_counter()
# print(counter) 



# debugging question
# debug 1
# def greet(): 
#    print("Hello")   
#    greet() 
# def greet(): 
#    print("Hello")  

# greet() 



# debug2
# def add(a, b):    
#     return a + b  
#     print(add(5)) 
# def add(a, b):   
#    return a + b  
# print(add(5,5))


# # debug3
# # def square(n)   
# # return n * n   
# # print(square(4)) 
# def square(n):     
#  return n * n   
# print(square(4)) 


# # debug4
# # def total(*args):    
# #     print(args + 1)  

# # total(1, 2, 3) 
# def total(*args):    
#     print(args , 1)   

# total(1, 2, 3) 

# # debug5
# # def show(): 
# #     print(x) 
# #     x = 10 
  
# # show() 
# def show(): 
#     x = 10 
#     print(x) 
  
# show()



# mini assignment
def Student_subject (subject1 = 0 , subject2 = 0 , subject3 = 0):
   total = subject1 + subject2 + subject3
   average = total / 3
   grade = lambda average: "A" if average >= 80 else "B" if average >= 60 else "C" if average >=60 else "Fail"
   print("total" , total)
   print("Average" , average)
   print("Grade"  , grade)

Student_subject(45 , 67 , 98)
Student_subject(98)