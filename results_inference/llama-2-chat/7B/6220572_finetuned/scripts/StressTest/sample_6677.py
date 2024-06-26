marks_premise = [96, 95, 82, 87, 92]
marks_hypothesis = [96, 95, 82, 87, 92]

# the hypothesis refers to the marks obtained in each subject mentioned in the premise
if any(marks_hypothesis[i] > marks_premise[i] for i in range(6)):
    # check if any of the marks in the hypothesis contradicts the marks reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
