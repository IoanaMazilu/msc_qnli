walked_days_premise = 7
walked_days_hypothesis = 3

if walked_days_hypothesis >= walked_days_premise:
    label = "entailment"
else:
    label = "contradiction"

print(label)
