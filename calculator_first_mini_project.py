print("***********WELCOME TO CALCULATOR*****************")
num1 = int(input("enter first number :"))
print(num1)
num2 = int(input("enter second number :"))
print(num2)
print("These are the oparators you can use ----- :")
print("1.Addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")
print("5.modulus")
result = 0
oparator = input("please choose an option from these(1,2,3,4,5):")
if oparator == '1':
    result=num1+num2
    print("The result of Additoion of", num1, "and", num2, "is", result)
if oparator == '2':
    if num1 < num2:

        print("Do not  subtract the first number less than second")
    else:

        result = num1 - num2
        print("The result of subtraction of", num1, "and", num2, "is", result)

if oparator == '3':
    if num2==0 or num1==0:
        print("canot multiple by zero")
    else:
        result=num1*num2
        print("The result of multiplication of", num1, "and", num2, "is", result)
if oparator == '4':
    if num2 == 0 :
        print("canot divisible by zero")
    else:
        result=num1//num2
        print("The result of division of", num1, "and", num2, "is", result)

if oparator == '5':
    if num2 == 0 :
        print("canot take modulus by zero")
    else:
        result=num1%num2
        print("The result of modulus of", num1, "and", num2, "is", result)
