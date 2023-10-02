
set1 = set()
set2 = set()

with open('text1.txt', 'r', encoding='utf8') as file:
    text = file.read()
    for symb in text:
        set1.add(symb)

with open('text2.txt', 'r',  encoding='utf8') as file:
    text = file.read()
    for symb in text:
        set2.add(symb)

print('1. Все символы, которые встречаются в двух заданных текстах:', set1 | set2)
print('2. Символы, которые встречаются в первом тексте, но не встречаются во втором:', set1 - set2)
print('3. Сколько различных символов:\nТекст 1:', len(set1), '\nТекст 2:', len(set2),
      '\nВсего:', len(set1 | set2))



