reema_marks_premise = 99
reema_marks_hypothesis = 35

# the hypothesis refers to the mark secured by Reema, which is mentioned in the premise
if reema_marks_premise <= reema_marks_hypothesis:
    # check if the estimate of'reema_marks_hypothesis' contradicts the mark secured by Reema in the premise
    label = "contradiction"
elif reema_marks_hypothesis!= reema_marks_premise:
    # check if the mark secured by Reema in the hypothesis contradicts the mark reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value and estimate do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
