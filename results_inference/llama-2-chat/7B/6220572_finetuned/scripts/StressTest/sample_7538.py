average_score_premise = 40
average_score_hypothesis = 40

# the hypothesis refers to the average score in different subjects mentioned in the premise
if average_score_hypothesis <= average_score_premise:
    # check if the hypothesis value contradicts the average score in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the average score
    # any average score greater than 'average_score_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
