average_score_premise = 38
average_score_hypothesis = 48

# the hypothesis refers to the average golf score mentioned in the premise
if average_score_premise > average_score_hypothesis:
    # check if the average score in the premise contradicts the estimate of less than 'average_score_hypothesis'
    label = "contradiction"
else:
    # if the average score in the premise does not contradict the estimate in the hypothesis, we can infer entailment
    label = "entailment"

print(label)
