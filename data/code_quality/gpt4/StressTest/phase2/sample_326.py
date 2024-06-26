amar_score_premise = 64
amar_score_hypothesis = 64
bhavan_score_premise = 36
bhavan_score_hypothesis = 36
chetan_score_premise = 44
chetan_score_hypothesis = 44

# the hypothesis talks about the scores of Amar, Bhavan, and Chetan, referenced also in the premise
if amar_score_hypothesis >= amar_score_premise:
    # check if the hypothesis value contradicts the estimate of less than 'amar_score_premise'
    label = "contradiction"
elif bhavan_score_hypothesis != bhavan_score_premise or chetan_score_hypothesis != chetan_score_premise:
    # check if the scores of Bhavan and Chetan in the hypothesis contradict the scores reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
