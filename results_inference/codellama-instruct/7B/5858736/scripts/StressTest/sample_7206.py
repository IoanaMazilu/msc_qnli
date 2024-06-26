marks_reema_premise = 35
marks_reema_hypothesis = 45

# the hypothesis talks about the marks secured by Reema, referenced also in the premise
if marks_reema_hypothesis >= marks_reema_premise:
    # check if the hypothesis value contradicts the estimate of less than'marks_reema_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the marks secured by Reema
    # any number of marks less than'marks_reema_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
