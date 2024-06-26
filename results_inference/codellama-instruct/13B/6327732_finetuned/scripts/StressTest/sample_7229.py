nancy_marks_premise = [66, 75, 52, 68, 89]
nancy_marks_hypothesis = [86, 75, 52, 68, 89]

# the hypothesis refers to the marks obtained by Nancy in the same subjects as the premise
if nancy_marks_hypothesis == nancy_marks_premise:
    # check if the hypothesis values contradict the premise values
    label = "entailment"
else:
    # the premise gives only an estimate for the marks obtained by Nancy
    # any number of marks greater than 'nancy_marks_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
