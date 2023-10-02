

with open('text.txt', 'r', encoding='utf8') as file:
    strings = file.readlines()

ans = {}

strings = [i.split() for i in strings]
print(strings)
new_strings = []
# смотрим строчку
for i in range(len(strings)):
    new_strings.append([])
    s = strings[i]
    # смотрим слово
    for w in s:
        # проверяем его посимвольно
        word = ''
        for symb in w:
            # если в нем не буква
            if not symb.isalpha():
                if word in ans.keys():
                    ans[word].add(i+1)
                elif word != '':
                    ans[word] = {i+1}
                word = ''
                continue
            else:
                word += symb

        if word == '':
            continue
        if word in ans.keys():
            ans[word].add(i + 1)
        else:
            ans[word] = {i + 1}


def print_dict():
    sorted_ans = sorted(ans.keys())
    for i in sorted_ans:
        print(f'{i}: {ans[i]}')


print_dict()



