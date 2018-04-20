''' Python program to find the
multiplication table (from 1 to 10)'''

num = 12

# To take input from the user
# num = int(input("Display multiplication table of? "))

# use for loop to iterate 10 times
for i in range(1, 11):
   print(num,'x',i,'=',num*i)

   # Python program to find the largest number among the three input numbers

   # change the values of num1, num2 and num3
   # for a different result
   num1 = 10
   num2 = 14
   num3 = 12

   # uncomment following lines to take three numbers from user
   # num1 = float(input("Enter first number: "))
   # num2 = float(input("Enter second number: "))
   # num3 = float(input("Enter third number: "))

   if (num1 >= num2) and (num1 >= num3):
       largest = num1
   elif (num2 >= num1) and (num2 >= num3):
       largest = num2
   else:
       largest = num3

   print("The largest number between", num1, ",", num2, "and", num3, "is", largest)