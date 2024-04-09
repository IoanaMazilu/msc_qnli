reema_marks_premise = 50
reema_marks_hypothesis = 70

# the hypothesis talks about the marks of Reema, referenced also in the premise
if reema_marks_hypothesis!= reema_marks_premise:
    # check if the marks of Reema in the hypothesis contradicts the marks of Reema reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
