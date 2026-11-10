while True:
    try:
        num1 = float(input("Введите число 1: "))
        num2 = float(input("Введите число 2: "))
    except ValueError:
        print("Операция отклонена, введено неверное значение!\n")
        continue
    oper = input("Введите оператор (+ - * /): ")
    if oper == "*":
        result = num1 * num2
    elif oper == "/" and num2 == 0:
        print("На ноль делить нельзя!\n")
        continue
    elif oper == "/":
        result = num1 / num2
    elif oper == "-":
        result = num1 - num2
    elif oper == "+":
        result = num1 + num2
    else:
        print("Неверный операто\n")
        continue
    print(f"{num1} {oper} {num2} = {result}\n")
    if input("Продолжаем? (да/нет): ") == "да":
        continue
    else:
        break
        
