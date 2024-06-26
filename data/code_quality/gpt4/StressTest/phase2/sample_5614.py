libi_score_premise = 68
libi_score_hypothesis = 78
nibi_score_premise = 75
nibi_score_hypothesis = 75
catherine_score_premise = 85
catherine_score_hypothesis = 85

# the hypothesis refers to the scores of Libi, Nibi, and Catherine mentioned in the premise
if libi_score_hypothesis <= libi_score_premise:
    # check if the hypothesis value contradicts the estimate of more than 'libi_score_premise'
    label = "contradiction"
elif nibi_score_hypothesis != nibi_score_premise or catherine_score_hypothesis != catherine_score_premise:
    # check if the scores of Nibi or Catherine in the hypothesis contradict the scores reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the score of Libi
    # any score of Libi greater than 'libi_score_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
