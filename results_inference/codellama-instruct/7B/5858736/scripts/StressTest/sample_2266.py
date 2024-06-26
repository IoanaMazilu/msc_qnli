glove_pairs_premise = 60
glove_pairs_hypothesis = 20

if glove_pairs_hypothesis >= glove_pairs_premise:
    label = "entailment"
else:
    label = "contradiction"

print(label)
