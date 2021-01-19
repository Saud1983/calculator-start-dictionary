from replit import clear
from art import logo

def add(num1,num2):
  return num1 + num2

def subs(num1,num2):
  return num1 - num2

def multi(num1,num2):
  return num1 * num2

def divied(num1,num2):
  return num1 / num2
  
oper = {
  '+':add,
  '-':subs,
  '*':multi,
  '/':divied
  }

new_cal = True

while new_cal:
  print(logo)
  counter = 1

  while counter > 0:
    if counter==1:
      counter=2
      num1=float(input("What's the first number?: "))
      for _ in oper:
        print(_)

    operation_selection=input("Pick an operation: ")
    num2=float(input("What's the next number?: "))
    cal=oper[operation_selection]
    answer=cal(num1,num2)
    print(f"{num1} {operation_selection} {num2} = {answer}")
    num1=answer
    continue_cal=input(f"Type 'y' to continue with {num1}, 'n' to start a new calculation: ")

    if continue_cal == 'n':
      counter=0
      clear()