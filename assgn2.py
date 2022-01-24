#q1
print("enter string")
#string is "Python is a case sensitive language"
string=input()
print("part a:")
print(len(string))
print("part b:")
slicestr=string[slice(9,26)]
print(slicestr)
print("part c:")
print(string[::-1])
print("part d:")
print(string.replace("a case sensitive","object oriented"))
print("part e:")
i=string.find('a')
print(i)
print("part f:")
print(string.replace(" ",""))
#q2
name=input("enter your name")
sid=input("what is your SID")
cgpa=input("mention cgpa")
department=input("department")
print("""Hey, %s Here!
My SID is %s
I am from %s department and my CGPA is %s"""%(name,sid,department,cgpa))
#q3
a=56
b=10
print("part a")
print(a&b)
print("part b")
print(a|b)
print("part c")
print(a^b)
print("part d")
print(a<<2)
print(b<<2)
print("part e")
print(a>>2)
print(b>>2)
#q4
a=input("enter ur first number")
b=input("enter ur second number")
c=input("enter ur third number")
if a>b and a>c:
    print("the greatest number is",a)
elif b>a and b>c:
    print("the greatest number is",b)
else:
    print("the greatest number is",c)
#q5
a=input("enter ur string")
if "name" in a:
    print("Yes")
else:
    print("No")
#q6
a=(float(input("lenth of first side")))
b=(float(input("length of second side")))
c=(float(input("length of third side")))
print(int(a))
print(int(b))
print(int(c))
if a>b+c or b>a+c or c>b+a:
    print("no, the triangle cannot be formed with these sides")
else:
    print("yes, the triangle can be formed with these sides")


    


