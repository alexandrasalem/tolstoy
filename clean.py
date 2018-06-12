import csv
from nltk import word_tokenize


filename = "anna_karenina_clean.txt"

with open(filename, "r") as f:
	text = f.read()

tokens = word_tokenize(text)
print(tokens[:100])
words = [word for word in tokens if word.isalpha()]
print(words[:100])

with open("new.csv", "w") as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow(words)

