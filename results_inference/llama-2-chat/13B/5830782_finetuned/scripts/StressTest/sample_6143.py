average_score_premise = 18
average_score_hypothesis = 38

# the hypothesis refers to the average golf score on the first four rounds mentioned in the premise
if average_score_hypothesis!= average_score_premise:
    # check if the average golf score in the hypothesis contradicts the average golf score reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
