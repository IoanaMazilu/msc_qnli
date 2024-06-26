walked_days_premise = 3
walked_days_hypothesis = 1

if walked_days_hypothesis <= walked_days_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
