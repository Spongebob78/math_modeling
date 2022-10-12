number0 = int(input())
number1 = int(input())

if number1 == 0:
  print("ошибка")
elif number0 % number1 == 0:
  print("число целое")
  print(number0 / number1)
elif number0 % number1 != 0:
  print("число не целое", number0 // number1, "остаток", number0 % number1)
  

  
