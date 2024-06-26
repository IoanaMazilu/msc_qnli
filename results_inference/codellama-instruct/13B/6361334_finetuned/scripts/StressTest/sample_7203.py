marks_reema_premise = 85
marks_reema_hypothesis = 60

# the hypothesis refers to the marks secured by Reema, which is also mentioned in the premise
if marks_reema_hypothesis >= marks_reema_premise:
    # check if the hypothesis value contradicts the marks secured by Reema in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the marks secured by Reema
    # any number of marks less than'marks_reema_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
