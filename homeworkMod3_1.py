

def single_root_words(root_word, * other_root_words):
    same_words = []
    for i in other_root_words:
        if root_word.lower() in i.lower() or i.lower() in root_word.lower():
            same_words.append(i)
    return same_words


results1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
results2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
results3 = single_root_words('Сыр', 'Сырой', 'Варить', 'Сыроварня', 'полусырой')
print(results1)
print(results2)
print(results3)