# Premise: If the marks secured by Reema was written as 46 instead of 56 then find the correct average marks up to two decimal places.
# Hypothesis: If the marks secured by Reema was written as less than 46 instead of 56 then find the correct average marks up to two decimal places.
# Golden Label: contradiction

reema_marks_premise = 46
reema_marks_written_hypothesis = 46
reema_marks_actual = 56

# the hypothesis talks about the marks of Reema mentioned in the premise
if reema_marks_written_hypothesis >= reema_marks_premise:
    # check if the written marks in hypothesis contradict the written marks in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

