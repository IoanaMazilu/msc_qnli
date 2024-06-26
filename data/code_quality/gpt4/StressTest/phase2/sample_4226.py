amar_score_premise = 84
bhavan_score_premise = 36
chetan_score_premise = 44

amar_score_hypothesis = 84
bhavan_score_hypothesis = 36
chetan_score_hypothesis = 44

# the hypothesis refers to the scores of Amar, Bhavan, and Chetan in an exam, mentioned in the premise
if amar_score_hypothesis >= amar_score_premise:
    # check if 'amar_score_hypothesis' contradicts the premise
    label = "contradiction"
elif bhavan_score_hypothesis != bhavan_score_premise or chetan_score_hypothesis != chetan_score_premise:
    # check if Bhavan's or Chetan's scores in the hypothesis contradict the scores reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
