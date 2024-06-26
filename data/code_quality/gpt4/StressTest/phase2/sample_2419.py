amar_score_premise = 44
amar_score_hypothesis = 64
bhavan_score_premise = 36
bhavan_score_hypothesis = 36
chetan_score_premise = 44
chetan_score_hypothesis = 44

# the hypothesis talks about the exam scores of Amar, Bhavan and Chetan, which are also referenced in the premise
if amar_score_hypothesis <= amar_score_premise:
    # check if the hypothesis value contradicts the estimate of more than 'amar_score_premise'
    label = "contradiction"
elif bhavan_score_hypothesis != bhavan_score_premise or chetan_score_hypothesis != chetan_score_premise:
    # check if the hypothesis values for Bhavan and Chetan contradict the values reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for Amar's score, and exact scores for Bhavan and Chetan
    # a score of Amar greater than 'amar_score_premise' and exact scores for Bhavan and Chetan are consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
