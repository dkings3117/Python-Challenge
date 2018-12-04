import os
import csv
bankCSV = os.path.join("Resources", "budget_data.csv")

def writeToScreenAndFile(csvwriter, str):
	print(str)
	csvwriter.writerow([str])

with open(bankCSV, 'r') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')
	header = next(csvreader)
	monthCount = 0
	totalProfitLoss = 0
	totalChange = 0
	lastMonthProfit = 0
	greatestIncrease = 0
	greatestDecrease = 0
	for row in csvreader:
		monthCount += 1
		totalProfitLoss += int(row[1])
		if monthCount > 1:
			change = int(row[1]) - lastMonthProfit
			totalChange += change
			if change > greatestIncrease:
				greatestIncrease = change
			elif change < greatestDecrease:
				greatestDecrease = change
		lastMonthProfit = int(row[1])
output_path = os.path.join("output.txt")
with open(output_path, 'w', newline='') as outfile:
	csvwriter = csv.writer(outfile, delimiter=',')
	writeToScreenAndFile(csvwriter, "Financial Analysis")
	writeToScreenAndFile(csvwriter, "------------------")
	writeToScreenAndFile(csvwriter, f"Total Months: {monthCount}")
	writeToScreenAndFile(csvwriter, f"Total: ${totalProfitLoss}")
	writeToScreenAndFile(csvwriter, f"Average Change: ${round(totalChange / (monthCount - 1), 2)}")
	writeToScreenAndFile(csvwriter, f"Greatest Increase in Profits: (${greatestIncrease})")
	writeToScreenAndFile(csvwriter, f"Greatest Decrease in Profits: (${greatestDecrease})")
