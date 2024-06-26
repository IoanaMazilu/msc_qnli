average_golf_score_premise = 88
average_golf_score_hypothesis = 58

# the hypothesis talks about the average golf score of Scott, which is also referenced in the premise
if average_golf_score_hypothesis >= average_golf_score_premise:
    # check if the hypothesis value contradicts the estimate of less than 'average_golf_score_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the average golf score
    # any average golf score less than 'average_golf_score_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
