from collections import defaultdict

# Чтение слов из файла
with open('[file_address]/words.txt', 'r') as file:
    words = file.read().split()

# Функция для получения множества символов в слове
def get_char_set(word):
    return set(word)

# Функция для проверки повторяющихся букв на тех же местах и подсчета их количества
def count_repeating_letters(word):
    seen = {}
    count = 0
    for index, letter in enumerate(word):
        if letter in seen:
            count += 1
        seen[letter] = index
    return count

# Функция для поиска повторяющихся букв между двумя словами на тех же позициях
def find_common_letters_at_same_positions(word1, word2):
    common_letters = []
    min_length = min(len(word1), len(word2))
    for i in range(min_length):
        if word1[i] == word2[i]:
            common_letters.append(word1[i])
    return common_letters

# Словарь для хранения слов по их символам
char_to_words = defaultdict(list)

# Заполнение словаря
for word in words:
    char_set = get_char_set(word)
    for char in char_set:
        char_to_words[char].append(word)

# Поиск и вывод слов с общими символами
words_with_common_chars = defaultdict(set)

for char, word_list in char_to_words.items():
    if len(word_list) > 1:
        for i in range(len(word_list)):
            for j in range(i + 1, len(word_list)):
                words_with_common_chars[(word_list[i], word_list[j])].add(char)

# Вывод результатов
if words_with_common_chars:
    print("Слова с общими символами и повторяющиеся символы между ними:")
    for word_pair, common_chars in words_with_common_chars.items():
        print(f"{word_pair[0]} и {word_pair[1]}: {', '.join(common_chars)}")
else:
    print("Нет слов с общими символами.")

# Поиск пары слов с наибольшим количеством общих символов
max_common_chars = 0
max_common_pair = None

for word_pair, common_chars in words_with_common_chars.items():
    if len(common_chars) > max_common_chars:
        max_common_chars = len(common_chars)
        max_common_pair = word_pair

# Вывод пары слов с наибольшим количеством общих символов
if max_common_pair:
    print("\nПара слов с наибольшим количеством общих символов:")
    print(f"{max_common_pair[0]} и {max_common_pair[1]}: {', '.join(words_with_common_chars[max_common_pair])} ({max_common_chars} общих символов)")
else:
    print("\nНет пары слов с общими символами.")

# Поиск и вывод слов с повторяющимися буквами на тех же местах
#repeating_words = [word for word in words if count_repeating_letters(word) > 0]

#if repeating_words:
#    print("\nСлова с повторяющимися буквами на тех же местах:")
#    for word in repeating_words:
#        print(word)
#else:
#    print("\nНет слов с повторяющимися буквами на тех же местах.")

# Поиск слова с наибольшим количеством повторяющихся букв на тех же местах
#max_repeating_count = 0
#max_repeating_word = None

#for word in words:
#    repeating_count = count_repeating_letters(word)
#    if repeating_count > max_repeating_count:
#        max_repeating_count = repeating_count
#        max_repeating_word = word

# Вывод слова с наибольшим количеством повторяющихся букв на тех же местах
#if max_repeating_word:
#    print("\nСлово с наибольшим количеством повторяющихся букв на тех же местах:")
#    print(f"{max_repeating_word}: {max_repeating_count} повторяющихся букв")
#else:
#    print("\nНет слов с повторяющимися буквами на тех же местах.")

# Поиск и вывод пар слов с повторяющимися буквами на тех же позициях
words_with_common_positions = defaultdict(list)

for i in range(len(words)):
    for j in range(i + 1, len(words)):
        common_letters = find_common_letters_at_same_positions(words[i], words[j])
        if common_letters:
            words_with_common_positions[(words[i], words[j])] = common_letters

# Вывод пар слов с повторяющимися буквами на тех же позициях
if words_with_common_positions:
    print("\nПары слов с повторяющимися буквами на тех же позициях:")
    for word_pair, common_letters in words_with_common_positions.items():
        print(f"{word_pair[0]} и {word_pair[1]}: {', '.join(common_letters)}")
else:
    print("\nНет пар слов с повторяющимися буквами на тех же позициях.")