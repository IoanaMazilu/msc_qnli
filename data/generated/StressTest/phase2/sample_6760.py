# Premise: If the marks secured by Reema was written as less than 56 instead of 56 then find the correct average marks up to two decimal places.
# Hypothesis: If the marks secured by Reema was written as 46 instead of 56 then find the correct average marks up to two decimal places.
# Golden Label: neutral

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

