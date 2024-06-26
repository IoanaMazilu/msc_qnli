average_score_premise = 46
average_score_hypothesis = 86

# the hypothesis refers to the average score in an examination mentioned in the premise
if average_score_hypothesis <= average_score_premise:
    # check if the hypothesis value contradicts the estimate of more than 'average_score_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the average score
    # any average score greater than 'average_score_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
