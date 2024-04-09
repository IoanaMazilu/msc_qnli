average_score_premise = 38
average_score_hypothesis = 48

# the hypothesis refers to the average golf score mentioned in the premise
if average_score_premise >= average_score_hypothesis:
    # check if the estimate of 'average_score_hypothesis' contradicts the average score in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
