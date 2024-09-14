import math

Vihod = True

while Vihod:
 a = float(input("Введите первое число: "))
 b = float(input("Введите второе число: "))


 operation = (input ("Введите операцию: +,-,*,/,**(Степень),sqrt: "))

 def Calculate (a, b, operation):

    if operation == '+':
      return a + b
    elif operation == '-':
      return a - b
    elif operation == '*':
      return a * b
    elif operation == '**':
      return a ** b
    elif operation == 'sqrt':
      if a >= 0:
       return math.sqrt (a)
    elif operation == '/':
      if b!= 0:
       return a / b
      else:
        return "Нельзя делить на ноль!"
    
    else :
      return "Некоретнная операция!"

    
 result = Calculate (a,b,operation)

 print(f"Результат операции: {result}")
 ansver = (input ("Хотите совершить повторную операцию? (Да/Нет) "))
 if ansver == "Нет" or "нет" :
   Vihod = False
   
    