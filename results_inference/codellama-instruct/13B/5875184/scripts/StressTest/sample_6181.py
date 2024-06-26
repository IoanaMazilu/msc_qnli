premise_marks = [16, 85, 82, 87, 85]
hypothesis_marks = [86, 85, 82, 87, 85]

# the hypothesis refers to the same subjects and marks as the premise
if premise_marks == hypothesis_marks:
    # check if the hypothesis values contradict the premise ones
    label = "contradiction"
else:
    # the premise gives only an estimate for the marks
    # any number of marks greater than the premise ones is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
