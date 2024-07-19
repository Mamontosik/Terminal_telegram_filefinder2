def load_words(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        words = file.read().split()
    return words

def find_common_characters(words):
    common_chars = []
    word_sets = {}
    word_pairs = {}
    
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            common = set(words[i]) & set(words[j])
            if common:
                common_chars.append((words[i], words[j], common))
                word_sets[words[i]] = word_sets.get(words[i], set()).union(common)
                word_sets[words[j]] = word_sets.get(words[j], set()).union(common)
                
                if words[i] not in word_pairs:
                    word_pairs[words[i]] = []
                if words[j] not in word_pairs:
                    word_pairs[words[j]] = []
                
                word_pairs[words[i]].append((words[j], len(common)))
                word_pairs[words[j]].append((words[i], len(common)))
    
    return common_chars, word_sets, word_pairs

def main():
    words = load_words('words.txt')
    common_characters, word_sets, word_pairs = find_common_characters(words)

    print("Пары слов с повторяющимися символами:")
    for word1, word2, common in common_characters:
        print(f"{word1} и {word2} имеют общие символы: {', '.join(common)}")

    print("\nСписок слов с повторяющимися символами:")
    for word, common in word_sets.items():
        print(f"{word} имеет общие символы: {', '.join(common)}")

    print("\nСписок слов и слов с которыми имеются общие символы (с наибольшим количеством общих символов):")
    for word, pairs in word_pairs.items():
        if pairs:
            max_common_word = max(pairs, key=lambda x: x[1])
            print(f"{word} имеет наибольшее количество общих символов с {max_common_word[0]}: {max_common_word[1]} символов")

if __name__ == "__main__":
    main()