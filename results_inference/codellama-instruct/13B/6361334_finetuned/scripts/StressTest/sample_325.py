amar_score_premise = 84
amar_score_hypothesis = 64
bhavan_score_premise = 36
bhavan_score_hypothesis = 36
chetan_score_premise = 44
chetan_score_hypothesis = 44

# the hypothesis refers to the scores of Amar, Bhavan and Chetan mentioned in the premise
if amar_score_hypothesis >= amar_score_premise:
    # check if the hypothesis value contradicts the estimate of less than 'amar_score_premise'
    label = "contradiction"
elif bhavan_score_hypothesis!= bhavan_score_premise:
    # check if the score of Bhavan in the hypothesis contradicts the score reported in the premise
    label = "contradiction"
elif chetan_score_hypothesis!= chetan_score_premise:
    # check if the score of Chetan in the hypothesis contradicts the score reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
