reema_marks_premise = 50
reema_marks_hypothesis = 70
correct_marks = 85

# the hypothesis refers to the marks secured by Reema mentioned in the premise
if reema_marks_premise!= correct_marks and reema_marks_hypothesis!= correct_marks:
    # check if the marks in the hypothesis contradict the correct marks mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
