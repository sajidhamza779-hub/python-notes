#11 november 2026

#CONDITIONALS

#if(to ask question)(check a condition)
#elif(to handle multiple conditions)
#<(less than)>(greater than)==(equals to)!=(not equals to)

x=int(input("value of x? "))
if x>10:
    print("greater")
elif x<10:
    print("less")

#or

x=int(input("value of x? "))
if x==10:
    print("equal")
elif x!=10:
    print("not equal")

#else(runs when no condition is met)

y=int(input("value of y? "))
if y==10:
    print("equal")
else:
    print("not equal")

#or(returns true if atleast 1 of the given conditions is true)
#and(returns true only if all given conditions are true)
#>=(greater than or equal to)
#<=(less than or equal to)

z=int(input("value of z? "))
if z>=10 or z==20:
    print("good")
elif z<=9 and z==5:
    print("bad")

#%(to find remainder in division)

x=int(input("what is x? "))
if x%2==0:
    print("even")
else:
    print("odd")

#match(Compares a value against multiple patterns and
#runs the code for the matching case)
#|(used as "or" in match)
#_(use as "else" in match)

name=input("what is your name? ")

match name:
    case "fawad khan" | "fahad mustufa":
        print("pakistan")
    case "shahrukh khan" | "salman khan":
        print("india")
    case _:
        print("not from india or pakistan")
