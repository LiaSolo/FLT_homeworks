lexeme_dict = {
    ':': 1,
    '(': 2,
    ')': 3,
    '.': 4,
    '*': 5,
    ';': 6,
    ',': 7,
    '#': 8,
    '[': 9,
    ']': 10,
    'Eofgram': 1000
}

free_number_to_use = {
    'nonterminal': [i for i in range(11, 51)],
    'terminal': [i for i in range(51, 101)],
    'semantics': [i for i in range(101, 151)]
}
non_or_terminal = []
spaces = []
brackets = []


# получаю список пробелов, которые надо вставить в начало соответствующих строк
def get_spaces():
    for g in grammar:
        space = ''
        for s in g:
            if s == ' ' or s == '\t':
                space += s
            else:
                break
        spaces.append(space)


# первым делом ищет нетерминалы по следующему двоеточию
def find_nonterminals():
    for line in strings:
        length = len(line)
        if length > 1:
            if line[1] == ':' and line[0] not in lexeme_dict.keys():
                try:
                    lexeme_dict[line[0]] = free_number_to_use['nonterminal'].pop(0)
                except IndexError:
                    raise Exception('Слишком много нетерминалов') from None


# первичная проверка (если можем, определяем что есть что и добавляем коды в ответ)
def get_pre_ans_one_line(num_line, line: list[str]) -> list[str, int]:
    pre_ans_one_line = []
    length = len(line)

    for i in range(length):
        word = line[i]
        temp = []
        if word not in lexeme_dict.keys():
            # семантика
            if word[0] == '$' and len(word) > 1:
                try:
                    lexeme_dict[word] = free_number_to_use['semantics'].pop(0)
                except IndexError:
                    raise Exception('Слишком много семантик') from None
            # терминалы
            elif (word[0] == "'" and word[-1] == "'") or word.islower():
                try:
                    lexeme_dict[word] = free_number_to_use['terminal'].pop(0)
                except IndexError:
                    raise Exception('Слишком много терминалов') from None
            # нетерминалы
            elif word.isupper():
                try:
                    lexeme_dict[word] = free_number_to_use['nonterminal'].pop(0)
                except IndexError:
                    raise Exception('Слишком много нетерминалов') from None
            else:
                for symb in word:
                    try:
                        temp.append(lexeme_dict[symb])
                    except KeyError:
                        raise Exception(f'Неопознанный объект.\n'
                                        f'Место ошибки: строка {num_line + 1}, слово {word}, символ {symb}') from None
        # известное слово или одиночный спецсимвол
        if word in lexeme_dict.keys():
            pre_ans_one_line.append(lexeme_dict[word])
        # разбираем по частям строку из спецсимволов
        elif len(temp) != 0:
            for t in temp:
                pre_ans_one_line.append(t)
        # если пока не можем сказать, терминал или нет
        else:
            pre_ans_one_line.append(word)
    return pre_ans_one_line


# проверяет, что все скобки спарены
def paired_brackets():
    for i in range(num_strings):
        for j in range(len(ans[i])):
            if ans[i][j] == 4:
                if len(brackets) > 0:
                    raise Exception(f'Неспаренные скобки\nМесто ошибки: строка {i + 1}') from None
            elif ans[i][j] == 2 or ans[i][j] == 9:
                brackets.append(ans[i][j])
            elif ans[i][j] == 3:
                try:
                    last_br = brackets.pop()
                    if last_br != 2:
                        raise IndexError
                except IndexError:

                    raise Exception(f'Неспаренные скобки ( и )\nМесто ошибки: строка {i + 1}') from None
            elif ans[i][j] == 10:
                try:
                    last_br = brackets.pop()
                    if last_br != 9:
                        raise IndexError
                except IndexError:
                    raise Exception(f'Неспаренные скобки [ и ]\nМесто ошибки: строка {i + 1}') from None


# красиво выводит коды с теми же отступами, как в исходном файле
def print_format():
    for i in range(num_strings):
        f_str = spaces[i]
        for code in ans[i]:
            f_str += str(code) + ' '
        print(f_str)


# красиво выводит словарь элемент-номер
def print_dict():
    lexeme_dict_revers = {x[1]: x[0] for x in lexeme_dict.items()}
    print(lexeme_dict_revers)

    for k in sorted(lexeme_dict_revers):
        print(f'{lexeme_dict_revers[k]}: {k}')


with open('test.txt', 'r') as file:
    grammar = file.readlines()
    num_strings = len(grammar)

get_spaces()
strings = [g.split() for g in grammar]
find_nonterminals()
ans = [get_pre_ans_one_line(i, strings[i]) for i in range(num_strings)]
print(ans)
paired_brackets()
print_format()
print_dict()
