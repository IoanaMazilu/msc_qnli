reema_marks_premise = 86
reema_marks_hypothesis = 36

# the hypothesis talks about the marks secured by Reema, referenced also in the premise
if reema_marks_hypothesis >= reema_marks_premise:
    # check if the hypothesis value contradicts the estimate of less than'reema_marks_premise'
    label = "contradiction"
elif reema_marks_hypothesis!= 66:
    # check if the hypothesis value contradicts the exact marks secured by Reema as per the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the marks of Reema
    # the exact marks of Reema as per the hypothesis is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
