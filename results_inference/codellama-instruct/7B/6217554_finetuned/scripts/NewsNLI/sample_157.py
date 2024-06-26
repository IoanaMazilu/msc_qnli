score_premise = 3
score_hypothesis = 3

# the hypothesis mentions the score in the second half, which is also referenced in the premise
if score_hypothesis!= score_premise:
    # check if the score in the hypothesis contradicts the score reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
