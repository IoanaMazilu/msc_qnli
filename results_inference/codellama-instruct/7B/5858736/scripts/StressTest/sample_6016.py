jane_age_premise = 40
jane_age_hypothesis = 20

if jane_age_hypothesis >= jane_age_premise:
    label = "entailment"
else:
    label = "contradiction"

print(label)
