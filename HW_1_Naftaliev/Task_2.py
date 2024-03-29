# Напишите код, который запрашивает число и сообщает является ли оно простым или составным. 
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”. 
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

a = int(input("Введите число от 0 до 100 000: "))

if a < 0 or a > 100000:
    print ("Ввидете допустимое значение от 0 до 100 000")
elif a == 1 or a == 0:
    print("По правилам математики число нельзя отнести ни к простым, ни к составным")
else:
    for i in range (2, int(a**0.5) + 1):
        if a % i == 0:
            print("Число составное")
            break
    print('Число простое')
