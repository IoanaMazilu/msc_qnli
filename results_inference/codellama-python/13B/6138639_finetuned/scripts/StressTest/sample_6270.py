participants_premise = 7
participants_hypothesis = 8

# the hypothesis refers to the number of participants in a cycling race mentioned in the premise
if participants_premise >= participants_hypothesis:
    # check if the number of participants in the premise contradicts the estimate of less than 'participants_hypothesis'
    label = "contradiction"
else:
    # if the premise values do not contradict the hypothesis ones, we can infer entailment
    label = "entailment"

print(label)
