# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. Дано a, b, c - стороны предполагаемого треугольника. 
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами 
# не существует. Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

a = int(input("Введите первую сторону треугольника: "))
b = int(input("Введите вторую сторону треугольника: "))
c = int(input("Введите Третью сторону треугольника: "))

if c > b + a or b > c + a or a > b + c:
    print ("Треугольник не существует")
elif a == b and a != c  or c == a and c != b or c == b and c != a :
    print ("Треугольник равнобедренный!")
elif a == b and a == c:
    print ("Треугольник равносторонний")
else:
    print('Обычный треугольник')