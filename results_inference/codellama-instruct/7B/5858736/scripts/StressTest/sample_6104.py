jane_age_premise = 18
jane_age_hypothesis = 58

if jane_age_hypothesis <= jane_age_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
