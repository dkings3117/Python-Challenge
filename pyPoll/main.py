import os
import csv
electionCSV = os.path.join("Resources", "election_data.csv")

def writeToScreenAndFile(csvwriter, str):
	print(str)
	csvwriter.writerow([str])

candidates = []
numVotes = []
with open(electionCSV, 'r') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')
	header = next(csvreader)
	totalVotes = 0
	for row in csvreader:
		totalVotes += 1
		candidate = row[2]
		if candidate not in candidates:
			candidates.append(candidate)
			numVotes.append(1)
		else:
			ind = candidates.index(candidate)
			numVotes[ind] = numVotes[ind] + 1
output_path = os.path.join("output","output.txt")
with open(output_path, 'w', newline='') as outfile:
	csvwriter = csv.writer(outfile, delimiter=',')
	writeToScreenAndFile(csvwriter, "Election Results")
	writeToScreenAndFile(csvwriter, "----------------")
	writeToScreenAndFile(csvwriter, f"Total Votes: {totalVotes}")
	writeToScreenAndFile(csvwriter, "----------------")
	maxVotes = 0
	maxInd = 0
	for candidate in candidates:
		ind = candidates.index(candidate)
		votePct = 100.0 * numVotes[ind] / totalVotes
		writeToScreenAndFile(csvwriter, f"{candidate}: {'%.3f' % votePct}% ({numVotes[ind]})")
		if numVotes[ind] > maxVotes:
			maxVotes = numVotes[ind]
			maxInd = ind
	writeToScreenAndFile(csvwriter, "----------------")
	writeToScreenAndFile(csvwriter, f"Winner: {candidates[maxInd]}")
	writeToScreenAndFile(csvwriter, "----------------")
