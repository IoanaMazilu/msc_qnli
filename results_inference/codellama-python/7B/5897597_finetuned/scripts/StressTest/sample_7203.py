reema_marks_premise = 50
reema_marks_hypothesis = 60
correct_marks_premise = 85
correct_marks_hypothesis = 85

# the hypothesis refers to the marks secured by Reema and the correct average marks, both mentioned in the premise
if reema_marks_hypothesis < reema_marks_premise:
    # check if the hypothesis value contradicts the marks secured by Reema in the premise
    label = "contradiction"
elif correct_marks_hypothesis!= correct_marks_premise:
    # check if the correct average marks in the hypothesis contradicts the correct average marks reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
