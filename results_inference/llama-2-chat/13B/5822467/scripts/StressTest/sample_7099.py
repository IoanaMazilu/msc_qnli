reema_marks_premise = 66
reema_marks_hypothesis = 36

# the hypothesis refers to the marks secured by Reema, which is also mentioned in the premise
if reema_marks_premise <= reema_marks_hypothesis:
    # check if the estimate of'reema_marks_hypothesis' contradicts the marks secured by Reema in the premise
    label = "contradiction"
elif reema_marks_hypothesis!= reema_marks_premise:
    # check if the marks secured in the hypothesis contradict the marks secured in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
