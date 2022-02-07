print("Created by Niclan051")
while(True):
    pervoechiclo=float(input("Enter the first number:\n"))
    deystvie=input("Choose from Addition, Substraction, Multiplication or Division:")
    vtoroechiclo=float(input("Enter the second number:\n"))
    if pervoechiclo!=int(pervoechiclo)or vtoroechiclo!=int(vtoroechiclo):
      print("Unable to calculate!")
    elif pervoechiclo==0and deystvie=="/"or vtoroechiclo==0and deystvie=="/":
      print("Unable to divide!")
    else:
      if deystvie=="Addition":
          print("Answer:",pervoechiclo+vtoroechiclo)
      if deystvie == "Substraction":
          print("Answer:",pervoechiclo-vtoroechiclo)
      if deystvie == "Multiplication":
          print("Answer:", pervoechiclo*vtoroechiclo) 
      if deystvie == "Division":
          print("Answer:", pervoechiclo/vtoroechiclo)