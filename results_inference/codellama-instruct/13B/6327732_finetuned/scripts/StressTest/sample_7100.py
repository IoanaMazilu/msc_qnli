marks_reema_premise = 66
marks_reema_hypothesis = 36

# the hypothesis refers to the number of marks secured by Reema, which is also mentioned in the premise
if marks_reema_hypothesis <= marks_reema_premise:
    # check if the hypothesis value contradicts the number of marks in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of marks
    # any number of marks greater than'marks_reema_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
