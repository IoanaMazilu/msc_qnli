reema_marks_premise = 35
reema_marks_hypothesis = 45

# the hypothesis refers to the marks secured by Reema mentioned in the premise
if reema_marks_premise >= reema_marks_hypothesis:
    # check if the estimate of'reema_marks_hypothesis' contradicts the marks secured by Reema in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
