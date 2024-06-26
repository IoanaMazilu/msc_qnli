reema_marks_premise = 46
reema_marks_hypothesis = 66
correct_marks = 96

# the hypothesis refers to the marks secured by Reema mentioned in the premise
if reema_marks_hypothesis == reema_marks_premise:
    # check if the hypothesis marks secured by Reema contradicts the marks secured by Reema in the premise
    label = "contradiction"
elif reema_marks_hypothesis != correct_marks:
    # check if the hypothesis marks secured by Reema contradicts the correct marks secured by Reema
    label = "contradiction"
else:
    # the premise gives a specific mark for Reema
    # the hypothesis gives a different specific mark for Reema, which is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
