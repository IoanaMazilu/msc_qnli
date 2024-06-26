reema_marks_premise = 35
reema_marks_hypothesis = 45

# the hypothesis refers to the marks secured by Reema mentioned in the premise
if reema_marks_premise > reema_marks_hypothesis:
    # check if the marks in the premise contradict the hypothesis
    label = "contradiction"
else:
    # if the premise marks do not contradict the hypothesis, we can infer entailment
    label = "entailment"

print(label)
