walked_days_premise = 2
walked_days_hypothesis = 3

if walked_days_hypothesis <= walked_days_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
