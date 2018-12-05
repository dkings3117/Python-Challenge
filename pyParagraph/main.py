import os
import csv
import re

infile = input("Please enter the name of the input file: ")
# infile = "paragraph_" + infileNumber + ".txt"
parCSV = os.path.join("Resources", infile)

def writeToScreenAndFile(csvwriter, str):
	print(str)
	csvwriter.writerow([str])

with open(parCSV, 'r') as text:
	wordCount = 0
	sentenceCount = 0
	letterCount = 0
	# print(text)
	# print("---------------")
	lines = text.read()
	pars = re.split("\n+", lines)
	# print(pars)
	# print("---------------")
	for par in pars:
		# print("---------------")
		sentences = re.split("[.!?] ", par)
		sentenceCount = sentenceCount + len(sentences)
		# print(sentences)
		# print("---------------")
		# print(f"sentenceCount = {sentenceCount}")
		# print("---------------")
		for sentence in sentences:
			words = re.split(" ", sentence)
			wordCount = wordCount + len(words)
			# print(words)
			for word in words:
				letterCount += len(word)
	# print("---------------")

output_path = os.path.join("output",infile)
with open(output_path, 'w', newline='') as outfile:
	csvwriter = csv.writer(outfile, delimiter=',')
	writeToScreenAndFile(csvwriter, "Paragraph Analysis")
	writeToScreenAndFile(csvwriter, "------------------")
	writeToScreenAndFile(csvwriter, f"Approximate word Count: {wordCount}")
	writeToScreenAndFile(csvwriter, f"Approximate Sentence Count: {sentenceCount}")
	writeToScreenAndFile(csvwriter, f"Average Letter Count: {'%.2f' % (letterCount / wordCount)}")
	writeToScreenAndFile(csvwriter, f"Average Sentence Length: {'%.2f' % (wordCount / sentenceCount)}")
