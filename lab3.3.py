s = str(input("Enter a sentence: "))
words = s.split()
letter_counts = {word: len(word) for word in words}

for word in letter_counts:
    count = letter_counts[word]
    print(f"Word '{word}' has {count} letters.")
