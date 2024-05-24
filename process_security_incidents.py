import csv

inputFile = 'security_incidents.csv'
outputFile ='security_incidents_modified.csv'

#Read the CSV file and store the data in a list.
with open(inputFile, mode='r') as infile:
    reader = csv.reader(infile)
    data = list(reader)

#Add a new column named Status with a default value of "Pending" for all rows.
newColumn = "Status"
defaultValue = "Pending"

# Add the new column to the header
header = data[0] + [newColumn]

# Add the new row to each row
row = [row + [defaultValue]for row in data[1:]]

#Save the modified data to a new CSV file named security_incidents_modified.csv.
with open(outputFile, mode='w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(header)
    writer.writerows(row)

print(f"Modified data saved to '{outputFile}'")
