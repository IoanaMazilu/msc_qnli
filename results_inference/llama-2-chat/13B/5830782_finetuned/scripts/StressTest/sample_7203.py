reema_marks_premise = 85
reema_marks_hypothesis = 60

# the hypothesis refers to the marks secured by Reema mentioned in the premise
if reema_marks_hypothesis <= reema_marks_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
