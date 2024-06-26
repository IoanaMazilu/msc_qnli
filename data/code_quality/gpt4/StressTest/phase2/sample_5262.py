average_score_premise = 68
average_score_hypothesis = 88

# the hypothesis refers to the average golf score mentioned in the premise
if average_score_hypothesis <= average_score_premise:
    # check if the estimate of 'average_score_hypothesis' contradicts the average score in the premise
    label = "contradiction"
elif average_score_hypothesis > average_score_premise:
    # check if the average score in the hypothesis is greater than the average score reported in the premise
    label = "neutral"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
