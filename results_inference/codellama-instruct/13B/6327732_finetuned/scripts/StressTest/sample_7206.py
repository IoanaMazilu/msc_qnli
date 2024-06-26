marks_reema_premise = 35
marks_reema_hypothesis = 45

# the hypothesis talks about the number of marks secured by Reema, referenced also in the premise
if marks_reema_hypothesis <= marks_reema_premise:
    # check if the hypothesis value contradicts the estimate of more than'marks_reema_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of marks
    # any number of marks greater than'marks_reema_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
