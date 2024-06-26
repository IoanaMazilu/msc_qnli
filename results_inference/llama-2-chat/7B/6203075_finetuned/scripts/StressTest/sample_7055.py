amar_score_premise = 64
bhavan_score_premise = 36
chetan_score_premise = 44

amar_score_hypothesis = 24
bhavan_score_hypothesis = 36
chetan_score_hypothesis = 44

# the hypothesis refers to the scores of Amar, Bhavan and Chetan in the exam
if amar_score_premise!= amar_score_hypothesis:
    # check if Amar's score in the hypothesis contradicts his score in the premise
    label = "contradiction"
elif bhavan_score_premise!= bhavan_score_hypothesis:
    # check if Bhavan's score in the hypothesis contradicts his score in the premise
    label = "contradiction"
elif chetan_score_premise!= chetan_score_hypothesis:
    # check if Chetan's score in the hypothesis contradicts his score in the premise
    label = "contradiction"
else:
    # if the hypothesis values and the premise values are the same, we can infer entailment
    label = "entailment"

print(label)
