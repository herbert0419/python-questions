#User will input (2numbers).Write a program to swap the numbers

# 1. using temp variable
num1 = int(input("Num1:"))
num2 = int(input("Num2:"))

print("Before swapping:", num1 ,num2)

temp = num1
num1=num2
num2 = temp

print("After swapping", num1, num2)


#using arithmetic operations

num1 = num1+num2
num2 = num1-num2
num1 = num1-num2

print("After swapping:", num1, num2)



