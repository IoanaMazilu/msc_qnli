# Premise: If the marks secured by Reema was written as 46 instead of 96 then find the correct average marks up to two decimal places.
# Hypothesis: If the marks secured by Reema was written as 66 instead of 96 then find the correct average marks up to two decimal places.
# Golden Label: contradiction

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

