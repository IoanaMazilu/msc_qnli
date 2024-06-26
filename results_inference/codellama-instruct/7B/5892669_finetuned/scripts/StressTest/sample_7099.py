reema_marks_premise = 86
reema_marks_hypothesis = 36

# the hypothesis talks about the marks secured by Reema, referenced also in the premise
if reema_marks_hypothesis >= reema_marks_premise:
    # check if the hypothesis value contradicts the estimate of less than'reema_marks_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the marks of Reema
    # any marks less than'reema_marks_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
