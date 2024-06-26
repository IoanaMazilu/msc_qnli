average_score_premise = 18
average_score_hypothesis = 38

# the hypothesis refers to the average golf score of Scott's first four rounds mentioned in the premise
if average_score_premise!= average_score_hypothesis:
    # check if the average golf score in the hypothesis contradicts the average golf score reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
