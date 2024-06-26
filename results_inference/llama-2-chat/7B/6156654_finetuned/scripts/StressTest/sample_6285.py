score_premise = 83
score_hypothesis = 70

# the hypothesis refers to the same scenario as the premise, but with a different score threshold
if score_hypothesis <= score_premise:
    # check if the hypothesis score is less than or equal to the premise score
    label = "entailment"
elif score_hypothesis > score_premise:
    # check if the hypothesis score is greater than the premise score
    label = "contradiction"
else:
    # if the hypothesis score is equal to the premise score, we cannot infer entailment or contradiction
    label = "neutral"

print(label)
