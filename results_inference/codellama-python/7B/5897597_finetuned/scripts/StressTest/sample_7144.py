average_score_premise = 48
average_score_hypothesis = 38

# the hypothesis refers to Scott's average golf score on his first four rounds, also mentioned in the premise
if average_score_hypothesis >= average_score_premise:
    # check if the hypothesis value contradicts the estimate of less than 'average_score_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the average score
    # any average score less than 'average_score_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
