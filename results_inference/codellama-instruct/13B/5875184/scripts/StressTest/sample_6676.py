premise_marks = [16, 95, 82, 87, 92]
hypothesis_marks = [96, 95, 82, 87, 92]

# the hypothesis refers to the exact marks obtained by Dacid in each subject
if hypothesis_marks == premise_marks:
    # check if the hypothesis values contradict the premise ones
    label = "contradiction"
else:
    # the premise gives only an estimate for the marks obtained by Dacid
    # any number of marks greater than the premise ones is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
