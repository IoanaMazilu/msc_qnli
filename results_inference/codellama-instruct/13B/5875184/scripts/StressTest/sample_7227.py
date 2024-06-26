nancy_marks_premise = [66, 75, 52, 68, 89]
nancy_marks_hypothesis = [86, 75, 52, 68, 89]

# the hypothesis talks about the number of marks obtained by Nancy in each subject
# the premise gives the exact marks obtained by Nancy in each subject
if nancy_marks_hypothesis <= nancy_marks_premise:
    # check if the hypothesis value contradicts the premise values
    label = "contradiction"
else:
    # the premise gives the exact marks obtained by Nancy in each subject
    # any number of marks greater than the premise values is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
