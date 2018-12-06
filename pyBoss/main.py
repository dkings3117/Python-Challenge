import os
import csv

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

employeeCSV = os.path.join("Resources", "employee_data.csv")

def writeToScreenAndFile(csvwriter, str):
	print(str)
	csvwriter.writerow([str])

output_path = os.path.join("output","output.csv")

with open(employeeCSV, 'r') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')
	header = next(csvreader)
	with open(output_path, 'w', newline='') as outfile:
		csvwriter = csv.writer(outfile, delimiter=',')
		csvwriter.writerow(["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"])
		for row in csvreader:
			empId = int(row[0])
			name = row[1]
			dobyyyymmdd = row[2]
			ssn = row[3]
			state = row[4]
			nameParts = name.split(' ', maxsplit=1)
			firstName = nameParts[0]
			lastName = nameParts[1]
			dobParts = dobyyyymmdd.split('-')
			yyyy = dobParts[0]
			mm = dobParts[1]
			dd = dobParts[2]
			dobmmddyyyy = mm + "/" + dd + "/" + yyyy
			ssnParts = ssn.split('-')
			ssn4 = "***-**=" + ssnParts[2]
			stateCode = us_state_abbrev[state]
			csvwriter.writerow([empId,firstName,lastName,dobmmddyyyy,ssn4,stateCode])
