import sys
import math

def discriminant(a,b,c):
    '''    
    a!=0
    '''
    if a==0:
        print("'a' must have nonzero value")
        sys.exit(1)
    return b*b-4*a*c

def roots(a,b,c):
    d=discriminant(a,b,c)
    print(d)
    if d<0:
        return (None,None)
    elif d>0:
        x1=(-b-math.sqrt(abs(d)))/(2*a)
        x2=(-b+math.sqrt(abs(d)))/(2*a)
        return (x1,x2)
    else:
        x1=-b/(2*a)
        return (x1,None)

def validate_input(prompt):
    c=3
    while c>0:
        try:
            n=float(input(prompt))
        except ValueError:
            c-=1
            if c==0:
                print('You have only 3 attempts for input')
            else:
                print('Please input any number')
            continue
        else:
            return n
    sys.exit(1)

def solution_output(a,b,c):
    x1, x2 = roots(a,b,c)
    print(f'Square equation: {a}x**2 + {b}*x + {c} = 0')
    print(f"Equation roots : {x1} and {x2}")

def main():
    # a!=0 will be checked in discriminant function
    solution_output(validate_input("a="),validate_input("b="),validate_input("c="))

main()