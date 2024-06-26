watermelons_premise = 536
watermelons_hypothesis = 136

if watermelons_hypothesis >= watermelons_premise:
    label = "entailment"
else:
    label = "contradiction"

print(label)
