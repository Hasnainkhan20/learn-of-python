# question 1
num1 = float(input("enter your number: "))
num2 = float(input("enter your number: "))
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)
print("Floor Division:", num1 // num2)
print("Modulus:", num1 % num2)
print("Exponent:", num1 ** num2)

# question 2
length = float(input("enter your lenght: "))
width = float(input("enter your widht: "))
area = length * width
perimeter = 2 * (length + width)
print("Area:", area)
print("Perimeter:", perimeter)

#  question 3
price = float(input("enter your price: "))
quantity = int(input("enter your quality: "))
total_bill = price * quantity
tax = total_bill * 0.05 # 5% tax
final_amount = total_bill + tax
print("Total Bill:", total_bill)
print("Tax 5%:", tax)
print("Final Amount:", final_amount)

# question 4
num1 = float(input("enter your num1: "))
num2 = float(input("enter your num2: "))
print("num1 > num2:", num1 > num2)
print("num1 < num2:", num1 < num2)
print("num1 == num2:", num1 == num2)

# question 5
marks = float(input("enter your student marks out of 100: "))

result = marks >= 40
print("Pass hai:", result)