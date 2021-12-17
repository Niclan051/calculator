print("Создатель: Михаил NicLan")
while(True):
    pervoechiclo=float(input("Введите первое число:\n"))
    deystvie=input("Выберите действие:\n+, -, * или /\n")
    vtoroechiclo=float(input("Введите второе число:\n"))
    if pervoechiclo!=int(pervoechiclo)or vtoroechiclo!=int(vtoroechiclo):
      print("Действие не может быть выполнено!")
    elif pervoechiclo==0and deystvie=="/"or vtoroechiclo==0and deystvie=="/":
      print("Действие не может быть выполнено!")
    else:
      if deystvie=="+":
          print("Ответ:",pervoechiclo+vtoroechiclo)
      if deystvie == "-":
          print("Ответ:",pervoechiclo-vtoroechiclo)
      if deystvie == "*":
          print("Ответ:", pervoechiclo*vtoroechiclo) 
      if deystvie == "/":
          print("Ответ:", pervoechiclo/vtoroechiclo)