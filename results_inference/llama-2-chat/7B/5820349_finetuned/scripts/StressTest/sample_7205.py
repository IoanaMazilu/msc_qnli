reema_marks_premise = 50
reema_marks_hypothesis = 70

# the hypothesis refers to the marks secured by Reema mentioned in the premise
if reema_marks_premise!= reema_marks_hypothesis:
    # check if the marks in the hypothesis contradicts the marks reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)