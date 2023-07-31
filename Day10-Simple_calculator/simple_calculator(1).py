#calculator
import art

print(art.logo)
def add(n1,n2):
  return n1+n2

def sub(n1,n2):
  return n1-n2

def mul(n1,n2):
  return n1*n2

def div(n1,n2):
  if n2==0:
    return "Division by zero is not possible"
  else:
    return n1/n2

calc={
  "+":add,
  "-":sub,
  "*":mul,
  "/":div
}
num1=int(input("enter 1st number\n"))
print("Choose the operator to be used to perform operation")
for oper in calc:
  print(oper)
op=input("enter the operator\n")
num2=int(input("enter 2nd number\n"))


if op=="+":
  answer=add(num1,num2)
elif op=="-":
  answer=sub(num1,num2)
elif op=="*":
  answer=mul(num1,num2)
elif op=="/":
  answer=div(num1,num2)

print(f"{num1} {op} {num2} = {answer}")

