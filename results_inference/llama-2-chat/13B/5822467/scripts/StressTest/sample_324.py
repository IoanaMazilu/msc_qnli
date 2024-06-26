amar_premise = 64
bhavan_premise = 36
chetan_premise = 44

amar_hypothesis = 84

# the hypothesis refers to the scores of Amar, Bhavan, and Chetan
if amar_hypothesis < amar_premise:
    # check if the estimate of Amar's score contradicts the premise
    label = "contradiction"
elif bhavan_hypothesis!= bhavan_premise:
    # check if the number of Bhavan's score in the hypothesis contradicts the premise
    label = "contradiction"
elif chetan_hypothesis!= chetan_premise:
    # check if the number of Chetan's score in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
