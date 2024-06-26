reema_marks_premise = 45
reema_marks_hypothesis = 35

# the hypothesis talks about the marks secured by Reema, referenced also in the premise
if reema_marks_hypothesis >= reema_marks_premise:
    # check if the hypothesis value contradicts the estimate of less than'reema_marks_premise'
    label = "contradiction"
elif reema_marks_hypothesis!= 35:
    # check if the hypothesis value contradicts the exact mark of Reema in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the marks of Reema
    # the hypothesis value is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
