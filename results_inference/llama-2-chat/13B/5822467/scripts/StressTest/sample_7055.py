amar_premise = 64
bhavan_premise = 36
chetan_premise = 44

amar_hypothesis = 24
bhavan_hypothesis = 36
chetan_hypothesis = 44

# the hypothesis refers to the scores of Amar, Bhavan, and Chetan in the exam
if amar_hypothesis <= amar_premise:
    # check if the estimate of 'amar_hypothesis' contradicts the score of Amar in the premise
    label = "contradiction"
elif bhavan_hypothesis!= bhavan_premise:
    # check if the score of Bhavan in the hypothesis contradicts the score of Bhavan reported in the premise
    label = "contradiction"
elif chetan_hypothesis!= chetan_premise:
    # check if the score of Chetan in the hypothesis contradicts the score of Chetan reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
