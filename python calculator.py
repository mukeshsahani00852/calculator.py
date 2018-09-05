#this is a calculator created by using python CODE---SELFP01
print("THIS IS CALCUATOR PROGRAM FOR ENTER IN PROGRAM PRESS true")
res=input("RESPONCE:::")
while res=="true":
  print("************************************************************************************************************************")
  print("TYPE ADD TO ADD TWO NUMBER") 
  print("TYPE MULTIPLY TO MULTIPLY TWO NUMBER")
  print("TYPE DIVIDE TO DIVIDE TO NUMBER")
  print("TYPE SUBTRACT TO SUBTRACT TWO NUMBER")
  print("TYPE REMENDER TO FIND REMENDER OF TWO NUMBER")
  responce=input("PLEASE ENNTER YOUR RESPINCE AND PRESS ENTER::::")
  print("************************************************************************************************************************")
  if responce=="ADD" or responce=="add":
     num1=float(input("PLEASE ENTER THE NUMBER1:::"))
     num2=float(input("PLEASE ENTER THE NUMBER2:::"))
     print("RESULT:::",num1+num2)
  elif responce=="MULTIPLY" or responce=="multiply":
     num1=float(input("PLEASE ENTER THE NUMBER1:::"))
     num2=float(input("PLEASE ENTER THE NUMBER2:::"))
     print("RESULT:::",num1*num2)
  elif responce=="divide" or responce=="DIVIDE":
     num1=float(input("PLEASE ENTER THE NUMBER1:::"))
     num2=float(input("PLEASE ENTER THE NUMBER2:::"))
     print("RESULT:::",num1/num2)
  elif responce=="subtract" or resonce=="SUBTRACT":
     num1=float(input("PLEASE ENTER THE NUMBER1:::"))
     num2=float(input("PLEASE ENTER THE NUMBER2:::"))
     print("RESULT:::",num1-num2)
  elif responce=="remender" or responce=="REMENDER":
     num1=float(input("PLEASE ENTER THE NUMBER1:::"))
     num2=float(input("PLEASE ENTER THE NUMBER2:::"))
     print("RESULT:::",num1%num2)
  print("***********************************************************************************************************************")
  cont=input("for exit press E for conitnue press c:::")
  if cont=='E' or cont=='e':
     break