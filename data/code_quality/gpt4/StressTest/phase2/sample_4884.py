average_score_premise = 28
average_score_hypothesis = 78

# the hypothesis refers to the average score of the first four rounds of golf mentioned in the premise
if average_score_hypothesis <= average_score_premise:
    # check if the hypothesis value contradicts the average score in the premise
    label = "contradiction"
elif average_score_hypothesis > average_score_premise:
    # since the hypothesized average score is greater than the premise average score, it does not contradict it
    # but it cannot be explicitly entailed from the premise either
    label = "neutral"
else:
    # if the hypothesis value and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
