# 1 Задание Сложная задача
Цена_за_килограмм = 34 # условия
Вес = 4.5 # условия
print(Цена_за_килограмм * Вес)

# 2 Задание  Сдача всем
price = int(input("Введите цену товара: "))
weight = float(input("Введите вес товара: "))
money = int(input("Введите сумму денег у покупателя: "))

cost = price * weight
change = money - cost
print(int(change))

# Задача 3
name = input("Введите название товара: ")
price = float(input("Введите цену товара за кг: "))
weight = float(input("Введите вес товара в килограммах: "))
money = float(input("Введите сумму денег от пользователя: "))

# общая стоимость товара и сдача
result = price * weight
change = money - result

# красивый чек
print(f"Чек {name} - {weight }кг - {price}руб/кг")
print(f"Итого: {result}руб")
print(f"Внесено: {money}руб")
print(f"Сдача: {change}руб")

 # Задача 4
N = int(input("Введите число: "))
for i in range(N):
    print("Купи конструктор!")

 # Задача Автоматизируем простоту
n = int(input("Введите число: "))
дело = input("Введите любимое дело: ")
for i in range(n) :
 print(f"Обожаю писать ' {дело}'!")




