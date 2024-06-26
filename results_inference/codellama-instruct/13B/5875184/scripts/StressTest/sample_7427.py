premise_marks = [76, 65, 82, 67, 85]
hypothesis_marks = [76, 65, 82, 67, 85]

# the hypothesis refers to the number of marks obtained in each subject
if hypothesis_marks <= premise_marks:
    # check if the hypothesis value contradicts the number of marks obtained in each subject in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of marks obtained in each subject
    # any number of marks greater than the premise marks is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
