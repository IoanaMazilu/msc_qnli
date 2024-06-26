score_premise = -2
score_hypothesis = -2

# the hypothesis mentions the starting score of the U.S. team, which is also mentioned in the premise
if score_hypothesis!= score_premise:
    # check if the starting score in the hypothesis contradicts the starting score reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
