balls_given_premise = 77
balls_given_hypothesis = 17

if balls_given_hypothesis <= balls_given_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
