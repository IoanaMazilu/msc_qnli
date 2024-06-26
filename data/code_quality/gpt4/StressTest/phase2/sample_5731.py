reema_marks_premise = 76
reema_marks_hypothesis = 46

# the hypothesis refers to a possible error in Reema's marks mentioned in the premise
if reema_marks_hypothesis != reema_marks_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
