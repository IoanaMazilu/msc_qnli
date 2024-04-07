# Premise: If the marks secured by Reema was written as 46 instead of 56 then find the correct average marks up to two decimal places.
# Hypothesis: If the marks secured by Reema was written as less than 56 instead of 56 then find the correct average marks up to two decimal places.
# Golden Label: entailment

reema_marks_premise = 46
reema_marks_hypothesis = 56

# the hypothesis refers to the marks secured by Reema mentioned in the premise
if reema_marks_hypothesis > reema_marks_premise:
    # check if the assumed 'reema_marks_hypothesis' contradicts the mark written in the premise
    label = "contradiction"
else:
    # if the hypothesis does not contradict the premise, we cannot infer entailment or contradiction
    label = "neutral"

print(label)

