from collections import Counter

# Sample text for analysis
text = """Python is easy to learn. Python is useful.
Learning Python helps students learn programming."""

# Convert all letters to lowercase
text = text.lower()

# Split the text into individual words
words = text.split()

# Count the total number of words
total_words = len(words)
print("Total words:", total_words)

# Count all characters in the original text
original_text = """Python is easy to learn. Python is useful.
Learning Python helps students learn programming."""

print("Total characters:", len(original_text))

# Count characters after removing spaces and new lines
characters = original_text.replace(" ", "").replace("\n", "")
print("Characters without spaces:", len(characters))

# Count vowels in the text
vowels = "aeiou"
total_vowels = 0

for letter in text:
    if letter in vowels:
        total_vowels += 1

print("Total vowels:", total_vowels)

# Find words that appear more than once
word_counts = Counter(words)

print("Repeated words:")
for word, count in word_counts.items():
    if count > 1:
        print(word, ":", count)
