#Date 24 octuber 2026
#print function(shows on screen)

print("hello, world")

#input function(asks for users input)
name=input("what is your name? ")
print("hello,", name)

#variable(stores value)
x=2244
print(x)

#this is comment(ignores code)

#str(string)
print("this is a str")

#end(to put nothing in end not even a new line)
print("hello", end="")
print("world")
#end2.0(to put something in end)
print("hello, world", end="...")

#sep(to seperate)
print("a","b","c", sep="-")

#\"(to put double quotes inside str)
print("are you \"serious\"")

#.strip()(to clear space from left and right)
print("    hello    ".strip())
#or
name=input("what is your name? ").strip()
print("hello, " +name)

#.title()(to capitalize every first letter)
print("hello world and universe".title())
#or
name=input("what is your name? ").title()
print("hello,", name)

#.split()(to break string into lists of smaller pieces)
name="ali,ahmed,khan".split(",")
print(name[0])
print(name[1])
print(name[2])
#or
x,y,z="1 2 3".split()
print(x)
print(y)
print(z)

#int(integer)(any number without decimal is integer)

#to convert str into int
x=int("5")
print(x+30)
#or
x="55"
print(int(x)-5)

#float(floating point)(any number with decimal is float)

#f"{}"(f string)(put variables inside a string)
name="hamza"
age="23"
print(f"my name is {name} and my age is {age}")

#:,(to put automaic commas btw numbers)
number=100000
print(f"{number:,}")

#round()(to round figure a float)
a=1.223
b=2.332
print(round(a+b))
#or
a=1.223
b=2.332
print(round(a+b,2))

#def(define)(to make function of your own)
def hello():
    print("hello,")

hello()
print("world")
#or
def hello(x):
    print("hello,", x)

name=input("what is your name? ")
hello(name)

#return(sends a value back from a function)
def name():
    return 5+5

print(name())
#or
def name(a, b):
    return a+b

print(name(5, 5))
#or
def main():
    x=int(input("what is x? "))
    print("x squared is,", squared(x))
    y=int(input("what is y? "))
    print("y doubled is,", doubled(y))

def squared(n):
    return n*n

def doubled(n):
    return n+n

main()
