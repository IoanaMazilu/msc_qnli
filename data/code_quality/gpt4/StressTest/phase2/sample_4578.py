amar_score_premise = 49
amar_score_hypothesis = 19
bhavan_score_premise = 36
bhavan_score_hypothesis = 36
chetan_score_premise = 44
chetan_score_hypothesis = 44

# the hypothesis refers to the scores of Amar, Bhavan and Chetan mentioned in the premise
if amar_score_premise <= amar_score_hypothesis:
    # check if the estimate of 'amar_score_hypothesis' contradicts Amar's score in the premise
    label = "contradiction"
elif bhavan_score_hypothesis != bhavan_score_premise:
    # check if Bhavan's score in the hypothesis contradicts Bhavan's score reported in the premise
    label = "contradiction"
elif chetan_score_hypothesis != chetan_score_premise:
    # check if Chetan's score in the hypothesis contradicts Chetan's score reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)