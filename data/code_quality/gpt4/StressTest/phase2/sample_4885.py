average_score_premise = 78
average_score_hypothesis = 28

# the hypothesis refers to Scott's average golf score, which is also mentioned in the premise
if average_score_hypothesis >= average_score_premise:
    # check if 'average_score_hypothesis' contradicts the average score in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the average score
    # any average score less than 'average_score_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
