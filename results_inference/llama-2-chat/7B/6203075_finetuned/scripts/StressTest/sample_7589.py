average_score_premise = 86
average_score_hypothesis = 86

# the hypothesis refers to the average score of Adam in the examination, which is also mentioned in the premise
if average_score_hypothesis <= average_score_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
