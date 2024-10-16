import re


class WordsFinder:
    file_name = []
    all_words = {}
    def __init__(self, *file_names):
        self.file_nam = file_names
        for file in self.file_nam:
            self.all_words[file] = []
            with open(file, 'r+', encoding='utf-8') as f:
                self.file_name.append(f)
    def get_all_words(self):
        for file_words in self.file_nam:
            with open(file_words, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.lower()
                    line= re.sub('[,.=!?;:-]', ' ', line)
                    for word in line.split():
                        self.all_words[file_words].append(word)
        return self.all_words

    def find(self, word):
        result = {}
        word = word.lower()
        for file_name, words in self.all_words.items():
            if word in words:
                result[file_name] = word
        return result

    def count(self, word):
        result_1 = {}
        word = word.lower()
        for file_name, words in self.all_words.items():
            if word in words:
                result_1[file_name] = words.count(word)
        return result_1



finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TeXt')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

