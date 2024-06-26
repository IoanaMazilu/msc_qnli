average_score_premise = 78
average_score_hypothesis = 78

if average_score_hypothesis <= average_score_premise:
    # check if the hypothesis value contradicts the estimate of more than 'average_score_premise'
    label = "contradiction"
elif average_score_hypothesis == average_score_premise:
    # check if the hypothesis value is equal to the premise one
    label = "neutral"
else:
    # any average score greater than 'average_score_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
