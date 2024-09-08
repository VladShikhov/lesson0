def single_root_words(root_word, *other_words):
    same_words = []
    root_word = root_word.lower()
    other_words_ = list(other_words)
    for i in range(len(other_words)):
        other_words_[i] = other_words_[i].lower()
        if root_word in other_words_[i] or other_words_[i] in root_word:
            same_words.append(other_words[i])
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)