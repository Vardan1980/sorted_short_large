def calculator(x,y,operation):
    if operation=='+':
        print(x+y)
    elif operation=='-':
        print(x-y)
    elif operation=='*':
        print(x*y)
    elif operation=='/' :
        print(x/y)
    else:
        print('EROR')
calculator(10,5,'+')
calculator(8,6,'-')
calculator(4,5,'*')
calculator(9,3,'/')
calculator(9,2,'**')