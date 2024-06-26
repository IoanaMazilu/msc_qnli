# Define variables for the scores
english_score = 66
mathematics_score = 60
chemistry_score = 72
biology_score = 77
french_score = 55
physics_score = 85

# Calculate the average mark scored by Andrea
total_score = english_score + mathematics_score + chemistry_score + biology_score + french_score + physics_score
average_score = total_score / 6

# Check if the hypothesis value contradicts the premise
if average_score <= 70:
    label = "contradiction"
else:
    label = "entailment"

print(label)
