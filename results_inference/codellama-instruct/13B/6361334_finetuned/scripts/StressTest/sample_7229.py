nancy_marks_premise = [66, 75, 52, 68, 89]
nancy_marks_hypothesis = [86, 75, 52, 68, 89]

# the hypothesis refers to the marks obtained by Nancy in the same subjects as the premise
if nancy_marks_hypothesis!= nancy_marks_premise:
    # check if the hypothesis values contradict the premise values
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
