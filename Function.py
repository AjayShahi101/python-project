# def CalculateDmean(a,b):
#     mean=(a*b)/(a+b)
#     print(mean)

# def isGreater(a,b):
#     if(a>b):
#         print("a is greater than b")
#     elif(b>a):
#         print("b is greater than a")
#     else:
#         print("b is equal to a")

# def isLesser(a,b):
#     pass


# a=int(input("Enter your number :"))
# b=int(input("Enter your no:"))
# CalculateDmean(a,b)
# isGreater(a,b)

# c=8
# d=5 
# CalculateDmean(c,d)  
# isGreater(c,d)


# def average(a=3,b=7):
#      print("avg of ",(a+b)/2)

# average(5)

# def name(fname="Kunjar", Mname ,Lname="Shahi"):
#     print("name is :",fname,Mname,Lname)

# name(Mname="Ajay")

def average(*numbers):
    total=0
    for i in numbers:
        total=total+i
    return total/len(numbers)

c=average(0,1,2,3,4,5,6,7,8,9)
print(c)

# tuple
# def average(*numbers):
#     print("Avg is :",sum(numbers)/len(numbers))

# average(1,2,3,4,5,6,7,8,9,10)