

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        words = []
        all_words = {}
        symbols = [',', '.', '=', '!', '?', ';', ':', ' -']
        for i in range(len(self.file_names)):
            with open(self.file_names[i], encoding='utf-8') as file:
                for line in file:
                    for n in range(len(symbols)):
                        if line.find(symbols[n]):
                            line = line.replace(symbols[n], '')
                    line = line.lower()
                    words += line.split()
                all_words[self.file_names[i]] = words
        return all_words

    def find(self, word):
        result = {}
        for name, words in self.get_all_words().items():
            for i in range(len(words)):
                if word.lower() == words[i]:
                    result[name] = i+1
                    break

        return result

    def count(self, word):
        result = {}
        count = 0
        for name, words in self.get_all_words().items():
            for i in range(len(words)):
                if word.lower() == words[i]:
                    count = count+1
            result[name] = count
        return result

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в текс