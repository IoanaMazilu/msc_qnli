average_score_premise = 88
average_score_hypothesis = 58

# the hypothesis refers to the average golf score mentioned in the premise
if average_score_hypothesis >= average_score_premise:
    # check if the average score in the hypothesis contradicts the premise's estimate of less than 'average_score_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the average score
    # any average score less than 'average_score_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
