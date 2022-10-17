
#2)generate fib series for 1 to 20
a = 0
b = 1
for i in range(1,20):
    c = a+b
    print(c)
    a,b=b,c
   
#1)write a func to take input from user in days and print it in year,month,days
days=int(input("Enter the no of days"))
year = days//365
days = days%365
month=days//30
days=days%30
print("year =",year)
print("month =",month)
print("days=",days)

#5)calculate the number of vowels individually i.e number of a, e, i , o and u , calculate total number of consonants without considering any punctuation character
s = "Python is a widely used general-purpose, high level programming language. It was created by Guido van Rossum in 1991 and further developed by the Python Software Foundation. It was designed with an emphasis on code readability, and its syntax allows programmers to express their concepts in fewer lines of code"
vowel_count = 0
cons_count = 0
for ch in s:
    if ch in "aeiouAEIOU":
        vowel_count += 1
    else:
        cons_count += 1
print("vowel_count is:",vowel_count)
print("cons_count is:",cons_count)

#6)Ask user a input string and check if the entered string is palindrome. Ex: Input NitiN -> o/p palindrome
name = input("Enter the string:")
for ch in name:
    if name == name[::-1]:
        print("string is palindrome")
    else:
        print("string is not palindrome")

#7)Ask user to input email and check if the email is in valid form or not. Ex: it should contain single '@', '.', @or.shouldn't be in 1st position
name = input("Enter the email:")
for i in name:
    if i in "@." and name.count(i[::-1])<=1:
        print("Entered email is valid")
    else:
        print("Entered email is not valid")
        

#9)Create a shopping cart for the below bakery_items using dictionary or list
bakery_items = {"Bread":40, "Butter":120, "Jam":200, "Cheese":220, "Crossiant":60}
cart = {}
print(bakery_items.keys())
for keys,values in bakery_items.items():
    if keys not in cart:
        cart[keys]=keys
print(cart.keys())
cart.update(sweet=266)
print(cart)
del cart['sweet']
print(cart)
        
