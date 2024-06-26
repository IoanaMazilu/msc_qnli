golf_score_premise = 48
golf_score_hypothesis = 38

if golf_score_hypothesis >= golf_score_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
