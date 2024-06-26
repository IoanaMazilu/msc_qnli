watermelons_premise = 700
watermelons_hypothesis = 200

if watermelons_hypothesis >= watermelons_premise:
    label = "entailment"
else:
    label = "contradiction"

print(label)
