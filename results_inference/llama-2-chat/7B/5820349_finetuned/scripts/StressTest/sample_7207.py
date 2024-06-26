reema_marks_premise = 45
reema_marks_hypothesis = 35
reema_marks_actual = 99

# the hypothesis refers to the marks secured by Reema mentioned in the premise
if reema_marks_hypothesis >= reema_marks_premise:
    # check if the hypothesis value contradicts the estimate of less than'reema_marks_premise'
    label = "contradiction"
elif reema_marks_hypothesis < reema_marks_actual:
    # the premise gives only an estimate for the marks
    # any marks less than'reema_marks_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
