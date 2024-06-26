average_score_premise = 50
average_score_hypothesis = 40

# the hypothesis scores are consistent with the premise scores, but cannot be explicitly entailed from the premise
if average_score_hypothesis <= average_score_premise:
    # check if the hypothesis value contradicts the estimate of more than 'average_score_premise'
    label = "contradiction"
else:
    # any score less than 'average_score_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
