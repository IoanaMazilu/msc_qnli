average_score_premise = 18
average_score_hypothesis = 38

# the hypothesis talks about the same average golf score of Scott mentioned in the premise
if average_score_premise != average_score_hypothesis:
    # check if the hypothesis value contradicts the average score mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
