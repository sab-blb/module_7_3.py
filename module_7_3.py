with open('test_file.txt', 'w', encoding='utf-8') as file:
    file.write("It's a text for task Найти везде,\n"
               "Используйте его для самопроверки.\n"
               "Успехов в решении задачи!\n"
               "text text text")

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']
        all_words = {}
        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    content = file.read().lower()
                    for punct in punctuation:
                        content = content.replace(punct, '')
                    words = content.split()
                    all_words[file_name] = words
            except FileNotFoundError:
                print(f"File {file_name} not found.")
                all_words[file_name] = []
        return all_words

    def find(self, word):
        word = word.lower()
        all_words = self.get_all_words()
        positions = {}
        for name, words in all_words.items():
            if word in words:
                positions[name] = words.index(word) + 1
            else:
                positions[name] = "Слово не найдено"
        return positions

    def count(self, word):
        word = word.lower()
        all_words = self.get_all_words()
        counts = {}
        for name, words in all_words.items():
            counts[name] = words.count(word)
        return counts


# Пример использования
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего


