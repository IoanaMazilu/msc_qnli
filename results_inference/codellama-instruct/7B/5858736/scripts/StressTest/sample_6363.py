watermelons_premise = 136
watermelons_hypothesis = 536

if watermelons_hypothesis >= watermelons_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
