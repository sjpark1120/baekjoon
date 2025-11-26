import sys
input = sys.stdin.readline

a = int(input())
operator = input().strip() 
b = int(input())

if(operator == '*'):
    print(a*b)
if(operator == '+'):
    print(a+b)
