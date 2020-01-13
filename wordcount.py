# put your code here.
# open file with open()
# for loop over each  line
# use split to split into words
# rstrip each line

#copy loop but change letter to word

def count_words_in_doc(file_name):

    word_counts = {}

    doc_data = open(file_name)
    for line in doc_data:
        line = line.rstrip()
        data = line.split(" ")

        for word in data:
            word = word.lower()
            word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts

word_counts = count_words_in_doc("test.txt")

def print_word_counts(word_counts):

    for word in word_counts:
        print(word, word_counts[word])



print_word_counts(word_counts)


# count_words_in_doc(word_counts)