# light=input("Enter the signal")
# if light ==("red"):
#     print("stop")
# elif light==("yellow"):
#     print("wait")
# elif light==("green"):
#     print("go")
# else :
#     print("invalid")


# marks=float(input("enter your grade "))
# if (marks >=90):
#     Grade="A"
# elif (marks >=80 and marks <90):
#     Grade="B"
# elif (marks >=70 and marks <80):
#     Grade="C"
# else:
#     Grade="D"
# print("Grade of the student -> ", Grade)


# a=int(input("Enter the number "))
# if a%2==0 :
#     print("number is even")
# else:
#     print("Number is odd")

# a=int(input("Enter the first number "))
# b=int(input("Enter the second number"))
# c=int(input("Enter the third number"))
# if (a>b and a>c):
#     print("a is the greatest number")
# elif (b>a and b>c):
#     print("b is the greatest number")
# else:
#     print("c is the greatest number ")

# list=[2,4,3,5]
# list.append(0)
# print(list) 
 
# d=[]
# a=input("Enter 1st movie: ")
# b=input("Enter 2nd movie")
# c=input("Enter 3rd movie ")

# d.append(a)
# d.append(b)
# d.append(c)
# print(d)

# list1=[1,2,1]
# list2=[1,2,3]
# copy_list1=list1.copy()
# copy_list1.reverse()

# if(copy_list1==list1):
#     print("Palindrome")
# else:
#     print("Non pelindrome")
  
# grade=["c" ,"d" ,"a" ,"a", "b","c"]
# grade.sort()
# print(grade )

# info={
#     "key":"value",
#     "name":"sumidson",
#     "learning":"coding",
#     "age":"18",
#     "is_adult":True,
#     "marks": 94.4

# }
# print(info)
# print(len(list(info.keys())))

# row=int(input())
# i=1

# while i<row+1:
#     k=1
#     while k<i+1:
#         print(i)


# n=int(input("Enter the number:"))
# for i in range(1,n):
#     for j in range(i):
#         # print("*",end='')
#         print(i,end='')
#     print("love you\n")



# for i in range(5):
#     for j in range(1,i+1):
#         print("*" ,end=" ")
#     print()

# n=int(input("Enter the number "))
# if n<=1:
#     print("Number is not prime")
# else:
#     is_prime=True
#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:
#             is_prime=False
#             break
# if is_prime:
#     print("prime")
# else:
#     print("not prime")

# x = "" or "default"

# print(type(10/2))

# a="hello" 
# print(a[1:5])

# n=int(input("Enter the number "))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print("*",end=" ")
#     print()

# info={
#     "name":"values",
#     "table":["a piece of furniture", "list of facts & figures"],
#     "cat":"a small animal"
# }
# print(info)

# x,y=map(int(input.split("Enter the number ")))

# subject={"python","java","c++","python","javascript","java","python","java","c++","c"}
# print(len(subject))

# marks={}

# x=int(input("enter physics marks: "))
# marks.update({"physics":x})
# y=int(input("enter chem marks:"))
# marks.update({"chem":y})
# print(marks)


# values={}
# x=float(input("Enter float number"))
# values.update({"float":x})
# y=int(input("Enter the integer number"))
# values.update({"integer":y})
# print(values)

# i=5 
# while i<6:
#     print(i)
#     i-=1
#     if i==1:
#         break
# print("loop ended")

# i=1
# while i<=100:
#     print(i)
#     i+=1

# n=int(input("Enter the number "))
# i=1
# while i<=10:
#     print(n*i)
#     i+=1
  

# n=[1,4,9,16,25,36,49,64,81,100]
# hero=["ironman" ,"thor","batman","superman"]
# i=0
# while i<len(hero):
#     print(hero[i])
#     i+=1
# while i<len(n):
#     print(n[i])
#     i+=1
 
# n=(1,4,9,16,25,36,49,64,81,100)
# i=0
# x=36 
# while i<len(n):
#     if(n[i]==x):
#         print("found the index",i)
#     else:
#         print("finding")
#     i+=1


# n=int(input("Enter the number"))
# s=1
# for i in range(1,n+n):
#     print(s)
#     s=s*2

# n=int(input("Enter the number"))
# if n<1:
#     print("Not prime ")
# if n==1:
#     print("Neither composite and prime")
# for i in range(2,n):
#     if n%i==0:
#       print("not prime")
#       break
# else:
#     if n==1:
#         print("Neither")
#     elif n<1:
#         print("not prime")
#     else:
#         print("prime")

# a=int(input())
# s=0
# fact=1
# for i in str(a):
#     for j in range(1,int(i)+1):
#         fact=fact*j
#     s=s+fact
#     fact=1
# if s==a:
#     print("y")
# else:
#     print("n")

# p=10
# q=20
# p*=q//3
# q+=p+q**2
# print(p, q)

# x=20
# x=x+5
# x=x-10
# print(x)
# x, y=x-1,50
# print (x, y)

# for i in range(-1,7,2):
#  for j in range(3):
#   print(i,j)

# string="aabbcc"
# count=3
# while True:
#     if string[0]=='a':
#       string=string[2:]
#     elif string[-1]=='b':
#       string=string[:2]
#     else:
#       count+=1
#       break
# print(string)
# print(count)

# x="hello world"
# print(x[2:-3],x[-4:-2])

# a=set('abc')
# b=set('cd')
# print(a^b)


# string = input("Enter a string: ")
# vowels = 'aeiouAEIOU'
# count = 0
# for i in string:
#     if i in vowels:
#         count += 1
# print("Number of vowels:", count)


# numbers = [5, 12, 7, 18, 3]
# for num in numbers:
#         if num > 10:
#             pass
#         else:
#             print(num)



