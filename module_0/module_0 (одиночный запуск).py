# код по угадыванию числа
import numpy as np
import math
number = np.random.randint(1,101)      # загадали число
print ("Загадано число от 1 до 100")
count = 50   # число, с которого начинается угадывание
count2 = 1
count3 = 1   # счетчик попыток
print("Попытка №",count3, "-", count)
while True:  # бесконечный цикл
    if number == count:
        break
    elif number < count:
        count2 = count2 * 2
        count = count - math.ceil(50/count2)
        count3 = count3 + 1
        print("Попытка №",count3, "-", count)
    else:
        count2 = count2 * 2
        count = count + math.ceil(50/count2)
        count3 = count3 + 1
        print("Попытка №",count3, "-", count)

print (f"Вы угадали число {number} за {count3} попыток.")

