amar_score_premise = 34
amar_score_hypothesis = 64
bhavan_score_premise = 36
bhavan_score_hypothesis = 36
chetan_score_premise = 44
chetan_score_hypothesis = 44

# the hypothesis refers to the scores of Amar, Bhavan, and Chetan mentioned in the premise
if amar_score_hypothesis <= amar_score_premise:
    # check if the score of Amar in the hypothesis contradicts the estimate of more than 'amar_score_premise'
    label = "contradiction"
elif bhavan_score_hypothesis != bhavan_score_premise or chetan_score_hypothesis != chetan_score_premise:
    # check if the scores of Bhavan and Chetan in the hypothesis contradict the scores reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the score of Amar
    # any score of Amar greater than 'amar_score_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
