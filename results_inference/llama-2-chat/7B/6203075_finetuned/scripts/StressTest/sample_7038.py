average_marks_premise = 56 + 60 + 72 + 85 + 80
average_marks_hypothesis = 26 + 60 + 72 + 85 + 80

# the hypothesis refers to the average marks of a student in specific subjects mentioned in the premise
if average_marks_hypothesis > average_marks_premise:
    # check if the average marks in the hypothesis contradicts the average marks in the premise
    label = "contradiction"
else:
    # if the average marks in the hypothesis do not contradict the average marks in the premise, we can infer entailment
    label = "entailment"

print(label)
