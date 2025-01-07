i = 0
print("think of a 2 to 3 digit number")
print("add 12 to it")
print("now add the digits together and subtract is from the original number (eg 23 = 2+3 = 5 = 23 - 5 = 18) ")
digits = (input ("how many digits are there in the number "))
if (digits == 2 ):
 num1 = ("enter the first number")
 if (i + num1 == 9):
   print ("your number is", num1 + "0" )
 else :
  while (num1 + i != 9):
   i += 1
   str(i)
   ans = num1 + i
    
if(digits == 3):
  num2 = ("enter the first and seconed  numbers")
else: 
  print ("not applicable pls make sure it is a three digit number")
