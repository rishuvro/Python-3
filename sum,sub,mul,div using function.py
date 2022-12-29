'''
Write down the functions Sum() ,Subtraction(), Multiplication() and
Division() which takes two number as floating type .

'''

def add(a, b):
    return a+b
def sub(a, b):
    return a-b
def mul(a, b):
    return a*b
def div(a, b):
    return a/b

print("Enter Two Numbers: ", end="")
num1 = float(input())
num2 = float(input())
print("Enter the Operator (+,-,*,/): ", end="")
i = input()
if i=='+':
    print("\n" +str(num1)+ " + " +str(num2)+ " = " +str(add(num1, num2)))
elif i=='-':
    print("\n" +str(num1)+ " - " +str(num2)+ " = " +str(sub(num1, num2)))
elif i=='*':
    print("\n" +str(num1)+ " * " +str(num2)+ " = " +str(mul(num1, num2)))
elif i=='/':
    print("\n" +str(num1)+ " / " +str(num2)+ " = " +str(div(num1, num2)))
    