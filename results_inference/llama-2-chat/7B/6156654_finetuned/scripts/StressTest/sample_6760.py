average_marks_premise = 56
average_marks_hypothesis = 46

# the hypothesis refers to the marks secured by Reema, which is also mentioned in the premise
if average_marks_hypothesis!= average_marks_premise:
    # check if the average marks in the hypothesis contradicts the average marks in the premise
    label = "contradiction"
else:
    # if the average marks in the hypothesis does not contradict the average marks in the premise, we can infer entailment
    label = "entailment"

print(label)
