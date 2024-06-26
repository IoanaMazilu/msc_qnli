marks_reema_premise = 50
marks_reema_hypothesis = 60

# the hypothesis refers to the marks secured by Reema mentioned in the premise
if marks_reema_premise >= marks_reema_hypothesis:
    # check if the estimate of'marks_reema_hypothesis' contradicts the marks in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
