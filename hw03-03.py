# 3. В большой текстовой строке подсчитать количество встречаемых слов и
# вернуть 10 самых частых. Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.
import re

MAX_OUT = 10

# текст берем из файла
file_txt = open('text.txt')
text = file_txt.read()
file_txt.close()

# убираем знаки препинания
new_text = re.sub(r'[^\w\s]', '', text)
# преобразование к нижнему регистру
text = new_text.lower()

# заполняем словарь частот
word_frequency = {}
text_list = text.split()
for i in text_list:
    word_frequency[i] = 1 if i not in word_frequency else word_frequency[i] + 1
print(word_frequency)

# выводим 10 максимальных от меньшего к большему
print(sorted(word_frequency, key=word_frequency.get)[-MAX_OUT:])
