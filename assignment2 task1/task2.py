#check the even or odd number

number=int(input("enter the number  "))
if number%2==0:
    print(number, "number is Even")
else:
    print(number, "number is Odd")

##Task 2: Sum of Integers from 1 to 50 Using a Loop

x = 0
for i in range(51):
    x += i
print("the sum of integers from 1 to 50 using a loop:",x )
