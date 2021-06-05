# Make a program that has some sentence (a string) on input and returns a dict containing all unique words
# as keys and the number of occurrences as values.

while True:
    answer = input('Would you like to use your own string? (y - yes, n - no): ')
    if answer.lower() == 'y' or answer.lower() == 'n':
        break
    print('Invalid value! Try again!')

if answer == 'n':
    requiredString = 'Ukraine is a country in Eastern Europe. It is the second largest country in Europe,' \
                         ' after Russia, which it borders to the east and north-east. Ukraine also shares borders ' \
                         'with Belarus to the north; Poland, Slovakia, and Hungary to the west; Romania and Moldova ' \
                         'to the south; and has a coastline along the Sea of Azov and the Black Sea'
else:
    requiredString = input()

# избавляемся от основных знаков препинания
requiredString = requiredString.replace('.', '').replace(',', '').replace('!', '').replace('?', '').replace(';', '')
# переводим в нижний регистр, чтобы слова в начале предложения не повторялись в словаре
temp_list = requiredString.lower().split()

result = dict((x, temp_list.count(x)) for x in temp_list)
print(result)
