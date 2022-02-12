# Pranay Patel, 20CE098
# AIM: You are given n words. Some words may repeat. For each word, output its number of occurrences.
# The output order should correspond with the input order of appearance of the word.
# github link : https://github.com/PranayPatel1707/python-basic-problems
n_ish = int(input())
counter_dict = {}
words_list = []

for i in range(n_ish):
    word = input()  # taking one word every time the loop runs
    words_list.append(word)  # we are adding the word to list
    if word in counter_dict:
        counter_dict[word] += 1  # if the word repeats, it's count is incremented
    else:
        counter_dict[word] = 1  # when a word appears for first time...count is initialized with 1

print(len(counter_dict))  # shows number of distinct words
print(' '.join([str(counter_dict[word]) for word in counter_dict]))  # shows the number of occurrences
