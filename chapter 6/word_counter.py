def count_word(sentence):
    unique_elements = set(sentence)
    counter = dict()
    for i in unique_elements:
        counter.update({
            i: sentence.count(i)
        })
    return counter


sentence = "This is the word counter program"
print(count_word(sentence))
