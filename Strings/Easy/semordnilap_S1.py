def semordnilap(words):
    word_set = set(words)
    list_semo = []
    for word in words:
        reverse = word[::-1]
        if reverse in word_set and reverse!=word:
            list_semo.append([word,reverse])
            word_set.remove(word)
            word_set.remove(reverse)
    return list_semo



            



words = ["dog", "hello", "desserts", "test", "god", "stressed"]
semordnilap = semordnilap(words)
print(semordnilap)