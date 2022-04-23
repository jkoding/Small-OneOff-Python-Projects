# Golf Score Reader
#
# This program reads golfer information from a file named 'results.txt'
# and displays the information in a formatted page. Data is created using
# a seperate program (GolfScoreWriter.py).

def main():
    # Variable declarations
    playerName = ''
    playerScore = 0

    # Setup Output
    print(f'Springfork Amateur Golf Club')
    print(f'{"Tournament Results" : ^28}')
    print('-' * 28)

    # Catch IOError in case file doesn't exist.
    try:
        # Open the file for reading.
        resultsFile = open('results.txt', 'r')

        # Prime the loop to detect end of line when done.
        # The first line is the player's name.
        playerName = resultsFile.readline()

        # Loop prints all records in file.
        while playerName != '':
            # Read the score of the player
            playerScore = resultsFile.readline()

            # Strip newlines from the fields.
            playerName = playerName.rstrip('\n')
            playerScore = playerScore.rstrip('\n')

            # Format and display the records.
            print(f'{playerName : >13} - {playerScore : >2}')

            # Read the next name in the file.
            playerName = resultsFile.readline()

        # Close the file.
        resultsFile.close()
    except IOError:
        print("Error occured when reading results.txt.")
        print("If file doesn't exist please run program GolfScoreWriter.py to make a new file.")


if __name__ == '__main__':
    main()
