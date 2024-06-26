marks_reema_premise = 56
marks_reema_hypothesis = 46

# the hypothesis refers to the marks secured by Reema mentioned in the premise
if marks_reema_hypothesis!= marks_reema_premise:
    # check if the marks in the hypothesis contradict the marks in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
