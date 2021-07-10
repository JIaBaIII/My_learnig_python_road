# № 1
chislo = int(input())
chislo_2 = (chislo % 2)
if chislo_2 == 0:
    print("ЧЁЁЁЁЁЁЁЁЁТКО!!! ☜(ﾟヮﾟ☜)")
else:
    print("Не чёёётко (☞ﾟヮﾟ)☞")

# ---------------------------------------------------------------------------------------------------------------------
# № 2
stringa = list(input())
nubmer_of_elements = len(stringa)
if nubmer_of_elements > 16:
    print("Нееее, Бать, это чёт много")
elif nubmer_of_elements < 16:
    print("Маловестенько, еще накати")
else:
    print("Самый, мать его, раз!!")

# ---------------------------------------------------------------------------------------------------------------------
# № 3
Letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
Numbers = ['1', '2', '3', '4', '5', '6', '7', '8']
print("Откуда начинаеем движение?")
start_moving = list(input())
print(start_moving)
print("Интересно.... И куда направляемся?)")
finish_move = list(input())
if start_moving[0] in Letters and start_moving[1] in Numbers\
        and finish_move[0] in Letters and finish_move[1] in Numbers:
    print('Поздравляю, вы на доске')
else:
    print('Что ж.... Это вылет с доски..ВЫ САМОЕ СЛАБОЕ ЗВЕНО - ПРОЩАЙТЕ')

