# 2. Треугольник существует только тогда, когда сумма любых двух его сторон
# больше третьей. Дано a, b, c - стороны предполагаемого треугольника.
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других,
# то треугольника с такими сторонами не существует. Отдельно сообщить является
# ли треугольник разносторонним, равнобедренным или равносторонним.

a = int(input('Введите длину стороны a: '))
b = int(input('Введите длину стороны b: '))
c = int(input('Введите длину стороны c: '))

if a == b == c:
    print("Треугольник существует и является равносторонним ")
elif a + b < c or a + c < b or b + c < a:  # указал бы '<=', нов условиях '<'
    print("Треугольник c такими сторонами не существует ")
elif a == b or a == c or b == c:
    print("Треугольник существует и является равнобедренным ")
else:
    print("Треугольник существует")
