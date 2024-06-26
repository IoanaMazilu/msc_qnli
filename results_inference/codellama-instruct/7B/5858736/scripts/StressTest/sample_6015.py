jane_age_premise = 20
jane_age_hypothesis = 40

if jane_age_hypothesis <= jane_age_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
