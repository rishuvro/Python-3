'''
 Write a Python program that takes five integer numbers from the user
and show the largest and smallest number.
'''

i = 0
largest = -float('inf')  
smallest = float('inf') 
while i < 5:
    i = i + 1

    a = input("enter the number")
    b = int(a)

  
    if b < smallest:
        smallest = b
    if b > largest:
        largest = b

print('the largest number is', largest)
print('the smallest number is', smallest)