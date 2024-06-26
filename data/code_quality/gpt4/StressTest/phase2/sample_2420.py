amar_score_premise = 64
amar_score_hypothesis = 64
bhavan_score_premise = 36
bhavan_score_hypothesis = 36
chetan_score_premise = 44
chetan_score_hypothesis = 44

# the hypothesis refers to the exam scores of Amar, Bhavan and Chetan mentioned in the premise
if amar_score_hypothesis <= amar_score_premise:
    # check if the hypothesis contradicts the premise in regards to Amar's score
    label = "contradiction"
elif bhavan_score_hypothesis != bhavan_score_premise:
    # check if the hypothesis contradicts the premise in regards to Bhavan's score
    label = "contradiction"
elif chetan_score_hypothesis != chetan_score_premise:
    # check if the hypothesis contradicts the premise in regards to Chetan's score
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
