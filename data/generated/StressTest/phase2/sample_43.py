# Premise: If the marks secured by Reema was written as more than 16 instead of 86 then find the correct average marks up to two decimal places.
# Hypothesis: If the marks secured by Reema was written as 36 instead of 86 then find the correct average marks up to two decimal places.
# Golden Label: neutral

reema_marks_premise = 16
reema_marks_hypothesis = 36
reema_actual_marks = 86

# The hypothesis refers to the marks secured by Reema mentioned in the premise
if reema_marks_hypothesis != reema_marks_premise:
    # check if the 'reema_marks_hypothesis' contradicts the 'reema_marks_premise' reported in the premise
    label = "contradiction"
elif reema_marks_hypothesis != reema_actual_marks or reema_marks_premise != reema_actual_marks:
    # The average marks can't be found without additional information, so the hypothesis can't be fully entailed from the premise
    label = "neutral"

print(label)
