reema_marks_premise = 35
reema_marks_hypothesis = 75
actual_reema_marks = 99

# the hypothesis refers to the marks secured by Reema, mentioned also in the premise
if reema_marks_hypothesis != reema_marks_premise:
    # check if the marks reported in the hypothesis contradict the marks reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
