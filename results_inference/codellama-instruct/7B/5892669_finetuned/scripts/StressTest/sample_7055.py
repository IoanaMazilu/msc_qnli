amar_score_premise = 64
amar_score_hypothesis = 24
bhavan_score_premise = 36
bhavan_score_hypothesis = 36
chetan_score_premise = 44
chetan_score_hypothesis = 44

# the hypothesis refers to the scores of Amar, Bhavan and Chetan mentioned in the premise
if amar_score_hypothesis!= amar_score_premise:
    # check if the score of Amar in the hypothesis contradicts the score of Amar reported in the premise
    label = "contradiction"
elif bhavan_score_hypothesis!= bhavan_score_premise:
    # check if the score of Bhavan in the hypothesis contradicts the score of Bhavan reported in the premise
    label = "contradiction"
elif chetan_score_hypothesis!= chetan_score_premise:
    # check if the score of Chetan in the hypothesis contradicts the score of Chetan reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
