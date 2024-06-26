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
