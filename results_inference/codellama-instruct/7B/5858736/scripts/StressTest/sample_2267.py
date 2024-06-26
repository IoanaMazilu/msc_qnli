glove_pairs_premise = 20
glove_pairs_hypothesis = 20

if glove_pairs_hypothesis <= glove_pairs_premise:
    label = "entailment"
else:
    label = "neutral"

print(label)
