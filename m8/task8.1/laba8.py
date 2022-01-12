import sys
import math

def discriminant(a,b,c):
    '''    
    function will return None if a==0
    '''
    if a==0:
        return None
        #0 unittest
    else:
        return b*b-4*a*c
        #1 unittest

def roots(a,b,c):
    d=discriminant(a,b,c)
    if d==None:
        x1="'a' must have nonzero value - don't worry"
        x2="be happy"
        #1 unittest
    elif d<0:
        x1="Nonreal"
        x2="Nonreal"
        #2 unittest
    elif d>0:
        x1=(-b-math.sqrt(abs(d)))/(2*a)
        x2=(-b+math.sqrt(abs(d)))/(2*a)
        #3 unittest
    else:
        x1=-b/(2*a)
        x2=None
        #4 unittest
    return (x1,x2)

def validate_input(prompt):
    # a!=0 will be checked in roots function
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
    try:
        x1, x2 = roots(a,b,c)
        print(f'Square equation: {a}x**2 + {b}*x + {c} = 0')
        print(f"Equation roots : {x1} and {x2}")
        return 0
    except:
        return 1

def main():
    solution_output(validate_input("a="),validate_input("b="),validate_input("c="))

main()