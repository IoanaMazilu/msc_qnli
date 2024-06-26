father_age_premise = 20
father_age_hypothesis = 10

if father_age_hypothesis <= father_age_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
