people_entered_premise = 15
people_entered_hypothesis = 15

if people_entered_hypothesis <= people_entered_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
