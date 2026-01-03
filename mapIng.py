from collections import Counter

strings = []
print(len(strings))
while True:
    try:
        user_input = input()
    except EOFError:
        break # завершаем ввод, если больше нет данных
    if user_input == '':
        break
    if user_input == 'Какой подарок?':
        count_dict = Counter(strings)
        duplicates = {item: count for item, count in count_dict.items()}
        print(duplicates.get('добрый'))
        if (duplicates.get('добрый') == duplicates.get('злой')):
            print('Ах, не знаю!')
        else:
            if duplicates.get('добрый') > duplicates.get('злой'):
                print('золотой шиллинг')
            else:
                print('серебряный шиллинг')
    else:
        print('Добавил')
        strings.append(user_input)

print(strings)