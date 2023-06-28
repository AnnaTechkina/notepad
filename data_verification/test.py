def get_letter(str):
    str = str.split()
    list = []
    for letter in str:
        sum_letter = 0
        for i in letter:
            if i in 'йуеыаоэяию':
                sum_letter += 1
        list.append(sum_letter)

    return len(list) == list.count(list[0])

poem = input("Введите стих: ")

if get_letter(poem):
    print('Парам пам-пам')
else:
    print('Пам парам')