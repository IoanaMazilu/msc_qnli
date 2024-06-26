reema_marks_premise = 35
reema_marks_actual = 99
reema_marks_hypothesis = 45

# the hypothesis refers to a condition similar to the premise
# it differs in the marks secured by Reema
if reema_marks_hypothesis > reema_marks_premise:
    # if the marks in the hypothesis are higher than the premise, it contradicts the premise
    label = "contradiction"
elif reema_marks_hypothesis < reema_marks_premise:
    # if the marks in the hypothesis are lower than the premise but less than the actual marks, it does not contradict the premise
    # however, it cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the marks in the hypothesis are equal to the premise, it can be entailed from the premise
    label = "entailment"

print(label)
