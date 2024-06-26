# define variables for the scores
english_score = 66
mathematics_score = 60
chemistry_score = 72
biology_score = 77
french_score = 55
physics_score = 85

# calculate the total score
total_score = english_score + mathematics_score + chemistry_score + biology_score + french_score + physics_score

# calculate the average score
average_score = total_score / 6

# check if the hypothesis value contradicts the premise
if average_score < 66:
    label = "contradiction"
else:
    label = "neutral"

print(label)
