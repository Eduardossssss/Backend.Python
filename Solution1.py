car_numbers = ["А123АА11", "А222АА123", "A12AA123", "A123CC1234",
               "AA123A12", "A1A123A12", "A454MM1", "О432РС159",
               "АВЕ12КA59", "A999НA99", "454MM1РСТ", "Х193ТТ01",
               "КРСТУСС22", "345435НОСТ", "Р233ТТ1345", "У323РТ12"]
letters = ["А", "В", "Е", "К", "М", "Н", "О", "Р", "С", "Т", "У", "Х"]

# Требованиями и условиями ГОСТа обозначено, что на автомобильных номерах могут быть использованы
# 12 букв из алфавита кириллицы — А, В, Е, К, М, Н, О, Р, С, Т, У и Х, так как только они имеют аналогичные буквы в латинице.
# Формат: буква — 3 цифры — 2 буквы, код региона.

def check_numbers(item):
    return item[0] in letters and item[1:4].isdigit() and item[4] in letters and item[5] in letters and item[6:].isdigit() and 8<=len(item)<=9


correct_numbers = [number for number in car_numbers if number[0] in letters
                   and number[1:4].isdigit()
                   and number[4] in letters
                   and number[5] in letters
                   and number[6:].isdigit()
                   and 8 <= len(number) <= 9]

print('\nИсходный список автомобильных номеров: {}'.format(car_numbers))
print('\nАвтомобильные номера отфильтрованы согласно ГОСТу: {}'.format(correct_numbers))
input('\nДля завершения программы нажмите ENTER.')