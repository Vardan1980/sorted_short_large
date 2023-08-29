users_database = ['Armen',0,'1234']
attempts = 0
cash_in = 0
cash_out = 0
def your_balance():
    print(f'Your balance is {users_database[1]} $')
def add_cash_in(sum):
    global cash_in
    cash_in += sum
def add_cash_out(sum):
    global cash_out
    cash_out += sum
def cashin():
    sum = int(input('Enter cash in sum =>>>'))
    if sum > 0:
        users_database[1] += sum
        print(f'Your balance increased {sum} $')
        your_balance()
        add_cash_in(sum)
    else:
        print('Bad command! Try again!')
        your_balance()
def cashout():
    sum = int(input('Enter cash out sum =>>>'))
    if sum < users_database[1]:
        users_database[1] -= sum
        print(f'Your balance decreased {sum} $')
        your_balance()
        add_cash_out(sum)
    else:
        print('Bad command! Try again!')
        your_balance()
def exit():
    print('E X I T')
while (True):
    if attempts == 3:
       break
    password = input('Enter your password =>>>')
    if password == users_database[2]:
       print(f'Welcome {users_database[0]} !!!')
       print('-'*30)
       print('Balance check = >>> press =>>> b')
       print('Cash in =>>> press =>>> +')
       print('Cash out =>>> press =>>> -')
       print('Days history =>>> press =>>> h')
       print('Want to exit =>>> press =>>> e')
       while (True):
           command = input('Enter your command =>>>')
           if command == 'b':
              your_balance()
           elif command == '+':
               cashin()
           elif command == '-':
               cashout()
           elif command == 'h':
               print(f'Today your balance increased {cash_in} $')
               print(f'Today your balance decreased {cash_out} $')
               your_balance()
           elif command == 'e':
               exit()
               break
           else:
               print('Bad command! Try again!')
    else:
       print('Wrong password! Try again!')
       attempts+=1