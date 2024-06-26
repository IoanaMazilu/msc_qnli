amar_score_premise = 24
amar_score_hypothesis = 64
bhavan_score_premise = 36
bhavan_score_hypothesis = 36
chetan_score_premise = 44
chetan_score_hypothesis = 44

# the hypothesis refers to the scores of Amar, Bhavan, and Chetan in an exam, mentioned also in the premise
if amar_score_hypothesis <= amar_score_premise:
    # check if Amar's score in the hypothesis contradicts the estimate of more than 'amar_score_premise'
    label = "contradiction"
elif bhavan_score_hypothesis != bhavan_score_premise or chetan_score_hypothesis != chetan_score_premise:
    # check if Bhavan's or Chetan's scores in the hypothesis contradict the scores reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for Amar's score
    # any score for Amar greater than 'amar_score_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
