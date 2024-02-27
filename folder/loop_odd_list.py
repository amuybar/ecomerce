# List of words
word_list = ["apple", "banana", "orange", "kiwi", "pear", "grape"]

# List comprehension to create a new list containing only words with an odd number of characters
odd_length_words = [word for word in word_list if len(word) % 2 != 0]

print("Words with odd number of characters:", odd_length_words)
