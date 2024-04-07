# Premise: If the marks secured by Reema was written as 36 instead of 86 then find the correct average marks up to two decimal places.
# Hypothesis: If the marks secured by Reema was written as more than 16 instead of 86 then find the correct average marks up to two decimal places.
# Golden Label: entailment

reema_marks_premise = 36
reema_marks_hypothesis = 16
correct_reema_marks = 86

# the hypothesis refers to the marks secured by Reema mentioned in the premise
if reema_marks_hypothesis >= reema_marks_premise:
    # check if the value of 'reema_marks_hypothesis' contradicts the marks mentioned in the premise
    label = "contradiction"
elif correct_reema_marks != reema_marks_premise:
    # check if the correct marks in the hypothesis contradicts the marks reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

