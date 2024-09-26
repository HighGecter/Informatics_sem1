def simplify(number):
    multipliers = []
    for i in range(2, number + 1):
        if number % i == 0:
            multipliers.append(i)
            number = number//i
    return multipliers

num = int(input())
print(f"Множители числа {num}:{simplify(num)}")