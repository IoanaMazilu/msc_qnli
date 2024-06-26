reema_marks_premise = 50
reema_marks_hypothesis = 70

# the hypothesis refers to the marks secured by Reema, mentioned also in the premise
if reema_marks_hypothesis!= reema_marks_premise:
    # check if the marks in the hypothesis contradict the marks reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
