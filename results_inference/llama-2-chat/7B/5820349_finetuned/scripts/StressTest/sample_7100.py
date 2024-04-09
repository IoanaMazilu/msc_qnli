reema_marks_premise = 36
reema_marks_hypothesis = 36

# the hypothesis refers to the marks of Reema mentioned in the premise
if reema_marks_hypothesis <= reema_marks_premise:
    # check if the hypothesis value contradicts the premise value of'reema_marks_premise'
    label = "contradiction"
else:
    # the premise gives a specific value for the marks of Reema
    # any value greater than'reema_marks_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
