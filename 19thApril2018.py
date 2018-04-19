# Python program to check if the number provided by the user is an Armstrong number or not

# take input from the user
# num = int(input("Enter a number: "))

# initialize sum
sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")

   # Program to display the Fibonacci sequence up to n-th term where n is provided by the user

   # change this value for a different result
   nterms = 10

   # uncomment to take input from the user
   # nterms = int(input("How many terms? "))

   # first two terms
   n1 = 0
   n2 = 1
   count = 0

   # check if the number of terms is valid
   if nterms <= 0:
       print("Please enter a positive integer")
   elif nterms == 1:
       print("Fibonacci sequence upto", nterms, ":")
       print(n1)
   else:
       print("Fibonacci sequence upto", nterms, ":")
       while count < nterms:
           print(n1, end=' , ')
           nth = n1 + n2
           # update values
           n1 = n2
           n2 = nth
           count += 1