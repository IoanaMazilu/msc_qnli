marks_reema_premise = 85
marks_reema_hypothesis = 70

# the hypothesis talks about the marks of Reema, referenced also in the premise
if marks_reema_hypothesis!= marks_reema_premise:
    # check if the marks in the hypothesis contradict the marks reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the marks
    # any marks consistent with the premise, but not equal to'marks_reema_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
