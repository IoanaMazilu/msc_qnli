premise_marks = [76, 65, 82, 67, 85]
hypothesis_marks = [46, 65, 82, 67, 85]

# the hypothesis refers to the exact marks obtained by Arun in each subject
if hypothesis_marks == premise_marks:
    # check if the hypothesis values contradict the premise ones
    label = "contradiction"
else:
    # the premise gives the exact marks obtained by Arun in each subject
    # any number of marks different from the premise ones is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
