# This program creates a SQL script containing INSERT commands using the data in a CSV file.
# The CSV should have the data in a 'clean' state so the output is exactly what you need for
# your insert commands. You do not have to use every column in the CSV, see the for loop in
# the script for more information.

import csv


# This example uses the records.csv file as an input and outputs to the nfl.sql file.
# Replace 'nfl.sql' to rename the output file as needed.
outputFile = open('nfl.sql', 'w')

# It is recommended that you edit and format the CSV file you will be using to include
# only the rows and columns needed prior to running.

# Replace 'records.csv' with the name of the CSV file you are using. The CSV should be
# in the same directory as this program.
# TODO - Add error handling, inform user of missing file.
with open('records.csv', 'r') as inputFile:
    reader = csv.reader(inputFile, delimiter=',')
    header = next(reader)

    # Match the columns here to the columns you want to include for your SQL values. If you open
    # the example records.csv you will notice some columns are skipped.
    for row in reader:
        team_name = row[0]
        team_conf = row[2]
        team_div = row[3]
        team_win = row[4]
        team_loss = row[5]
        team_tie = row[6]
        team_sup_win = row[7]
        team_sup_loss = row[8]

        # Format the string to match the values from the above for loop. You can change this as needed.
        line = f"""INSERT INTO TEAM\nVALUES\n('{team_name}', '{team_conf}', '{team_div}',{team_win},{team_loss},{team_tie},{team_sup_win},{team_sup_loss});\n\n"""
        outputFile.write(line)

outputFile.close()
inputFile.close()
