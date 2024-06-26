score_premise = [20, 6]
score_hypothesis = [20, 6]

# the hypothesis mentions the game result, which is also referenced in the premise
if score_hypothesis != score_premise:
    # check if the game result in the hypothesis contradicts the game result reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
