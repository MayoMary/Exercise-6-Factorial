# Mary McHale, 27th March 2018
# Exercise 6 based on 
# Asked to " Write a Python script that containing a function called factorial() that takes a single input/argument which is a positive integer and returns its factorial."
# Source of Iris dataset was https://en.wikipedia.org/wiki/Iris_flower_data_set






n = input ("Please type a positive number between 1 and 20: ")
n=int(n)
print (n)
m = n + 1
a = 1
c = 1

while c < m:
    a = a * c
    c = c + 1

print(a, "is the answer.")

