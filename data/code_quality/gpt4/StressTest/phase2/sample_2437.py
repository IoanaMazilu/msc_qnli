amar_score_premise = 54
amar_score_hypothesis = 64
bhavan_score_premise = 36
bhavan_score_hypothesis = 36
chetan_score_premise = 44
chetan_score_hypothesis = 44

# the hypothesis refers to the scores of Amar, Bhavan and Chetan in an exam, also mentioned in the premise
if amar_score_hypothesis <= amar_score_premise:
    # check if the 'amar_score_hypothesis' contradicts the estimate of more than 'amar_score_premise'
    label = "contradiction"
elif bhavan_score_hypothesis != bhavan_score_premise:
    # check if Bhavan's score in the hypothesis contradicts his score in the premise
    label = "contradiction"
elif chetan_score_hypothesis != chetan_score_premise:
    # check if Chetan's score in the hypothesis contradicts his score in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for Amar's score
    # Amar's score in the hypothesis is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
