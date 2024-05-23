reema_marks_premise = 56
reema_marks_hypothesis = 46

# the hypothesis refers to the marks secured by Reema mentioned in the premise
if reema_marks_hypothesis >= reema_marks_premise:
    # check if the hypothesis value contradicts the estimate of less than'reema_marks_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the marks
    # any marks less than'reema_marks_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)