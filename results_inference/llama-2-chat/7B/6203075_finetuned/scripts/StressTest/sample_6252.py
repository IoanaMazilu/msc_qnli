scores_premise = 1
scores_hypothesis = 7

# the hypothesis refers to the scores in the game, which are also mentioned in the premise
if scores_hypothesis < scores_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
