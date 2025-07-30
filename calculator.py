num1 = int(input("Enter the First Number : \n"))
validop = [ "+","-","*","/"]

for i in validop : 
  oprator = input ( "Enter the oprator : \n")
  if oprator in validop :
    num2 = int(input("Enter the Second Number : \n"))
    break
  else : 
    print("Please Enter the Correct Oprator ⛔⚠️:\n ")

if (oprator == "+" ) : 
   print(f"{num1} + {num2} = {num1 + num2}\n")
elif (oprator == "*" ) : 
   print(f"{num1} X {num2} = {num1 * num2}\n")
elif (oprator == "-" ) : 
   print(f"{num1} - {num2} = {num1 - num2}\n")
else : 
   print(f"{num1} / {num2} = {num1 / num2}\n")

 