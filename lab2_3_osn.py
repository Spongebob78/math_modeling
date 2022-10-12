number0 = int(input())

if number0 % 4 == 0 and number0 % 100 != 0 or number0 % 400 == 0:
  print("високосный")
else:
  print("невисокосный")