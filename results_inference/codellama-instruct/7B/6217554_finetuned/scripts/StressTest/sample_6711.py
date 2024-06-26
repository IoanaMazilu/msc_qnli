balls_given_premise = 17
balls_given_hypothesis = 77

if balls_given_hypothesis <= balls_given_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
