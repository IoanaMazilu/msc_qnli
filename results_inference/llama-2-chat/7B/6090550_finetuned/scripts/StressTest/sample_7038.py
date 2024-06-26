average_marks_premise = [56, 60, 72, 85, 80]
average_marks_hypothesis = [26, 60, 72, 85, 80]

# the hypothesis refers to the average marks obtained in each subject mentioned in the premise

# the hypothesis also refers to the marks obtained in each subject mentioned in the premise

if average_marks_premise <= average_marks_hypothesis:
    # check if the average marks in the hypothesis contradicts the average marks in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
