def load_words(filename):
    # Открываем файл для чтения и считываем все слова, разделенные пробелами
    with open(filename, 'r', encoding='utf-8') as file:
        words = file.read().split()
    return words

def find_common_characters(words):
    # Инициализируем списки и словари для хранения результатов
    common_chars = []
    word_sets = {}
    word_pairs = {}
    
    # Проходим по всем парам слов
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            # Находим общие символы между двумя словами
            common = set(words[i]) & set(words[j])
            if common:
                # Добавляем пару слов и их общие символы в список
                common_chars.append((words[i], words[j], common))
                
                # Обновляем словари для хранения общих символов для каждого слова
                word_sets[words[i]] = word_sets.get(words[i], set()).union(common)
                word_sets[words[j]] = word_sets.get(words[j], set()).union(common)
                
                # Обновляем словари для хранения пар слов и количества общих символов
                if words[i] not in word_pairs:
                    word_pairs[words[i]] = []
                if words[j] not in word_pairs:
                    word_pairs[words[j]] = []
                
                word_pairs[words[i]].append((words[j], len(common)))
                word_pairs[words[j]].append((words[i], len(common)))
    
    return common_chars, word_sets, word_pairs

def main():
    # Загружаем слова из файла
    words = load_words('words.txt')
    
    # Находим общие символы между словами
    common_characters, word_sets, word_pairs = find_common_characters(words)

    # Выводим пары слов с общими символами
    print("Пары слов с повторяющимися символами:")
    for word1, word2, common in common_characters:
        print(f"{word1} и {word2} имеют общие символы: {', '.join(common)}")

    # Выводим список слов с их общими символами
    print("\nСписок слов с повторяющимися символами:")
    for word, common in word_sets.items():
        print(f"{word} имеет общие символы: {', '.join(common)}")

    # Выводим список слов и слов, с которыми у них наибольшее количество общих символов
    print("\nСписок слов и слов с которыми имеются общие символы (с наибольшим количеством общих символов):")
    for word, pairs in word_pairs.items():
        if pairs:
            max_common_word = max(pairs, key=lambda x: x[1])
            print(f"{word} имеет наибольшее количество общих символов с {max_common_word[0]}: {max_common_word[1]} символов")

if __name__ == "__main__":
    # Запускаем основную функцию
    main()