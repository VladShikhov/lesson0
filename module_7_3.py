import io


class WordsFinder:

    def __init__(self, *args):
        self.file_names = list(args)

    def get_all_words(self):
        all_words = {}
        punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for i in range(len(self.file_names)):
            with open(self.file_names[i], 'r', encoding='utf-8') as file:
                file_as_list = file.read().split()
                for j in range(len(file_as_list)):
                    file_as_list[j] = file_as_list[j].lower()
                    if file_as_list[j][-1] in punctuation:
                        file_as_list[j] = file_as_list[j][:len(file_as_list[j])-1]
                all_words[self.file_names[i]] = file_as_list
        return all_words
    
    def find(self, word):
        word = word.lower()
        word_num = {}
        all_words = WordsFinder.get_all_words(self)
        for key in all_words:
            if word in all_words[key]:
                value = all_words[key].index(word) + 1
                word_num[key] = value
            else:
                continue
        return word_num
    
    def count(self, word):
        word = word.lower()
        word_quantity = {}
        all_words = WordsFinder.get_all_words(self)
        for name, words in all_words.items():
            count = 0
            if word in words:
                for word_ in words:
                    if word == word_:
                        count += 1
            word_quantity[name] = count
        return word_quantity



finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

# finder2 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt', 
#                       'Rudyard Kipling - If.txt', 
#                       "Mother Goose - Monday’s Child.txt")
# print(finder2.get_all_words()) # Все слова
# print(finder2.find('the')) # 3 слово по счёту
# print(finder2.count('the')) # 4 слова teXT в тексте всего

    
    

