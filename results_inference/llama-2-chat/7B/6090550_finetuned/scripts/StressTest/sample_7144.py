 score_premise = 48
score_hypothesis = 38

# the hypothesis talks about the average golf score of Scott's first four rounds, which is also mentioned in the premise
if score_hypothesis >= score_premise:
    # check if the hypothesis value contradicts the estimate of less than'score_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the average score
    # any average score less than'score_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
