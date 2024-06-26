reema_marks_premise = 56
reema_marks_hypothesis = 46

# the hypothesis refers to Reema's marks in the premise
if reema_marks_hypothesis >= reema_marks_premise:
    # check if the hypothesis value contradicts the premise (Reema's marks are less than 56)
    label = "contradiction"
else:
    # the premise gives only an estimate for Reema's marks
    # any mark less than 'reema_marks_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
