reema_marks_premise = 99
reema_marks_hypothesis = 45

# the hypothesis refers to the marks secured by Reema, which is also mentioned in the premise
if reema_marks_hypothesis >= reema_marks_premise:
    # check if the hypothesis value contradicts the estimate of less than'reema_marks_premise'
    label = "contradiction"
else:
    # if the hypothesis value is less than'reema_marks_premise', it is consistent with the premise
    # but we cannot infer entailment because we cannot determine the correct average marks in this case
    label = "neutral"

print(label)
