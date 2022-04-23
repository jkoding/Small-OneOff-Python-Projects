# Golf Score Writer
#
# This program will accept user input for a golfer's name and their scores.
# The data collected will be written as results to a text file to
# be used by a seperate program.

def main():
    # Variable Declarations
    golferName = ''
    golferScore = 0

    playerCount = get_integer_input('count')
    # Open a new file named results.txt
    resultsFile = open('results.txt', 'w')

    # Get input from user for all golfers
    for count in range(1, playerCount + 1):
        print(f'Enter info for golfer {count}:')
        golferName = input('Player name: ')
        golferScore = get_integer_input('score')

        resultsFile.write(f'{golferName}\n')
        resultsFile.write(f'{golferScore}\n')

    resultsFile.close()


def get_integer_input(validationType):
    """Get an integer from user input and validate.

    This function returns an integer from user input.
    Validation constraints are determined by the parameter. 

    Args:
        validationType (str): Determines what input validation to perform.
            If set to 'score': get and validate player score.
            If set to 'count': get and validate player count.
    Raises:
        Exception: if parameter is not 'count' or 'score'.   

    Returns:
        an integer.

    """
    # Func variables
    scoreErrorMessage = "Invalid score entered, please try again.(Score should be between 18 and 144)"
    countErrorMessage = "Sorry, that is not a proper amount, please enter whole numbers that are larger than 0."
    MAX_SCORE = 144
    MIN_SCORE = 18
    MIN_PLAYERS = 1

    # Loop for proper input.
    while True:
        try:
            if (validationType == 'score'):
                score = int(input("Player score: "))
            elif (validationType == 'count'):
                count = int(input('How many golfers played?\n'))
            else:
                raise ValueError("Parameter is not 'count' or 'score'.")
        # Change error message depending on what we are validating.
        except ValueError:
            if validationType == 'score':
                print(scoreErrorMessage)
                continue
            if validationType == 'count':
                print(countErrorMessage)
                continue
        else:
            # Validate the integer is within proper constraints.
            if validationType == 'score':
                if MIN_SCORE <= score <= MAX_SCORE:
                    return score
                else:
                    print(scoreErrorMessage)
                    continue
            elif validationType == 'count':
                if MIN_PLAYERS <= count:
                    return count
                else:
                    print(countErrorMessage)
                    continue


if __name__ == '__main__':
    main()
