pounds_premise = 4
pounds_hypothesis = 8

if pounds_hypothesis <= pounds_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
