# The marks scored by Adam in the premise
spanish_mark_premise = 85
math_mark_premise = 67
biology_mark_premise = 52
physics_mark_premise = 69
french_mark_premise = 56
fine_art_mark_premise = 62
chemistry_mark_premise = 59

# The marks scored by Adam in the hypothesis
spanish_mark_hypothesis = 15
math_mark_hypothesis = 67
biology_mark_hypothesis = 52
physics_mark_hypothesis = 69
french_mark_hypothesis = 56
fine_art_mark_hypothesis = 62
chemistry_mark_hypothesis = 59

# Calculating the average mark in the premise
average_mark_premise = (spanish_mark_premise + math_mark_premise + biology_mark_premise + physics_mark_premise + french_mark_premise + fine_art_mark_premise + chemistry_mark_premise) / 7

# Calculating the average mark in the hypothesis
average_mark_hypothesis = (spanish_mark_hypothesis + math_mark_hypothesis + biology_mark_hypothesis + physics_mark_hypothesis + french_mark_hypothesis + fine_art_mark_hypothesis + chemistry_mark_hypothesis) / 7

# If the average mark in the hypothesis is more than the average mark in the premise, then it is a contradiction
if average_mark_hypothesis > average_mark_premise:
    label = "contradiction"
# If the average mark in the hypothesis is equal to the average mark in the premise, then it is entailment
elif average_mark_hypothesis == average_mark_premise:
    label = "entailment"
# If the average mark in the hypothesis is less than the average mark in the premise, then it is neutral
else:
    label = "neutral"

print(label)
