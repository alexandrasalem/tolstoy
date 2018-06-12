import csv
from nltk import word_tokenize

def clean(infilename, outfilename):
	title = outfilename[:-4]
	with open(infilename, "r") as f:
		text = f.read()

	tokens = word_tokenize(text)
	tokens = [w.lower() for w in tokens]
	print(tokens[:100])
	words = [word for word in tokens if word.isalpha()]
	print(words[:100])

	with open(outfilename, "w") as csvfile:
		writer = csv.writer(csvfile)
		writer.writerow(["title", "words"])
		for word in words:
			writer.writerow([title, word])

names = [["anna_karenina_clean.txt", "anna_karenina.csv"], ["boyhood_clean.txt", "boyhood.csv"], 
		["childhood_clean.txt", "childhood.csv"], ["cossacks_clean.txt", "cossacks.csv"],
		["resurrection_clean.txt", "resurrection.csv"], ["war_and_peace_clean.txt", "war_and_peace.csv"],
		["youth_clean.txt", "youth.csv"]]

for name in names:
	clean(name[0], name[1])
