reema_marks_premise = 36
reema_marks_hypothesis = 36

# the hypothesis refers to the marks of Reema mentioned in the premise
if reema_marks_hypothesis <= reema_marks_premise:
    # check if the estimate of'reema_marks_hypothesis' contradicts the marks of Reema in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
