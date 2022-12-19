import math


# Calculate the final score of a competition
def calculate_final_score(scores):
    # Check if there are at least 3 judges
    if len(scores) < 3:
        raise ValueError('There must be at least 3 judges')

    # Check if all scores are between 0 and 10
    for score in scores:
        if score < 0 or score > 10:
            raise ValueError('Scores must be between 0 and 10')

    # Sort the scores in ascending order
    scores.sort()

    # Remove the highest and lowest scores
    scores = scores[1:-1]

    # Calculate the average of the remaining scores
    final_score = sum(scores) / len(scores)

    return final_score


# Get the scores from the user
scores = []
num_judges = int(input('Enter the number of judges: '))
for i in range(num_judges):
    score = int(input(f'Enter score for judge {i + 1}: '))
    scores.append(score)

# Calculate and print the final score
try:
    final_score = calculate_final_score(scores)
    print(f'Final score: {final_score:.2f}')
except ValueError as e:
    print(e)
