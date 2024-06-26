reema_marks_premise = 50
reema_marks_hypothesis = 70
correct_marks = 85

# the hypothesis talks about the marks of Reema, referenced also in the premise
if reema_marks_hypothesis!= reema_marks_premise:
    # check if the hypothesis value contradicts the value of Reema's marks in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
