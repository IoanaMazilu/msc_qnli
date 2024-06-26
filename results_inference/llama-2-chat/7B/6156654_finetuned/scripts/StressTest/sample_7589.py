average_score_premise = 86 + 75 + 72 + 63 + 65
average_score_hypothesis = 86 + 75 + 72 + 63 + 65

# the hypothesis refers to the same scores as the premise, but with a different threshold
if average_score_hypothesis >= average_score_premise:
    label = "entailment"
elif average_score_hypothesis < average_score_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
