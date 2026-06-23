def reverse_sentence(sentence):
    words_list = sentence.split()
    print(f"Original sentence in list format: {words_list}")
    words_list.reverse()
    print(f"Reversed sentence in list format: {words_list}")
    final_sentence = ' '.join(words_list)
    return final_sentence
result = reverse_sentence("python is easy to learn")
print(f"Reversed sentence: {result}")
