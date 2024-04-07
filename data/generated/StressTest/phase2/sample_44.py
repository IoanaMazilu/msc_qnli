# Premise: If the marks secured by Reema was written as 36 instead of 86 then find the correct average marks up to two decimal places.
# Hypothesis: If the marks secured by Reema was written as more than 36 instead of 86 then find the correct average marks up to two decimal places.
# Golden Label: contradiction

reema_marks_premise = 36
reema_correct_marks = 86
reema_marks_hypothesis = 36

# the hypothesis refers to the marks secured by Reema, which is also mentioned in the premise
if reema_marks_hypothesis <= reema_marks_premise:
    # check if the hypothesis value contradicts the estimate of more than 'reema_marks_hypothesis'
    label = "contradiction"
else:
    # the premise gives only an estimate for the marks of Reema
    # any marks greater than 'reema_marks_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

