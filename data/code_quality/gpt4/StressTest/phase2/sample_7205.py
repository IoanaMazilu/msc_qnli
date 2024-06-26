reema_marks_premise = 50
reema_correct_marks = 85
reema_marks_hypothesis = 70

# the hypothesis refers to the marks secured by Reema mentioned in the premise
if reema_marks_premise != reema_correct_marks:
    # check if the 'reema_marks_premise' contradicts the correct marks of Reema
    label = "contradiction"
elif reema_marks_hypothesis != reema_correct_marks:
    # check if the 'reema_marks_hypothesis' contradicts the correct marks of Reema
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
