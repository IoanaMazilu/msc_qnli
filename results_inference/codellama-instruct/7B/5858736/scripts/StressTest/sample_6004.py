balls_premise = 10
balls_hypothesis = 4

if balls_hypothesis <= balls_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
