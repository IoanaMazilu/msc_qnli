amar_score_premise = 84
amar_score_hypothesis = 64
bhavan_score_premise = 36
bhavan_score_hypothesis = 36
chetan_score_premise = 44
chetan_score_hypothesis = 44

# the hypothesis refers to the scores of Amar, Bhavan and Chetan mentioned in the premise
if amar_score_hypothesis >= amar_score_premise:
    # check if the hypothesis value of 'amar_score_hypothesis' contradicts the premise
    label = "contradiction"
elif bhavan_score_hypothesis!= bhavan_score_premise:
    # check if the hypothesis value of 'bhavan_score_hypothesis' contradicts the premise
    label = "contradiction"
elif chetan_score_hypothesis!= chetan_score_premise:
    # check if the hypothesis value of 'chetan_score_hypothesis' contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
