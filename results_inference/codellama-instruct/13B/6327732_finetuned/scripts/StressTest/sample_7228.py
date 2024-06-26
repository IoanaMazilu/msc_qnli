nancy_marks_premise = [86, 75, 52, 68, 89]
nancy_marks_hypothesis = [66, 75, 52, 68, 89]

# the hypothesis refers to the exact marks obtained by Nancy in each subject, as mentioned in the premise
if nancy_marks_hypothesis!= nancy_marks_premise:
    # check if the hypothesis values contradict the premise values
    label = "contradiction"
else:
    # the premise gives exact marks obtained by Nancy in each subject
    # any number of marks greater than 'nancy_marks_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
