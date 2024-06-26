glove_pairs_premise = 20
glove_pairs_hypothesis = 60

if glove_pairs_hypothesis >= glove_pairs_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
