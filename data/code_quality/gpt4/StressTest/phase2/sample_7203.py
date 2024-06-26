reema_marks_premise = 50
reema_marks_actual = 85
reema_marks_hypothesis = 60

# the hypothesis refers to the marks of Reema mentioned in the premise
if reema_marks_hypothesis >= reema_marks_premise:
    # check if the hypothesis value contradicts the premise of 'reema_marks_premise'
    label = "contradiction"
elif reema_marks_hypothesis == reema_marks_premise:
    # check if the hypothesis value is equal to the premise of 'reema_marks_premise'
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)
