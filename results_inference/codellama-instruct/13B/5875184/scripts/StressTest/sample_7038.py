premise_marks = [56, 60, 72, 85, 80]
hypothesis_marks = [26, 60, 72, 85, 80]

# the hypothesis refers to the number of marks obtained by the student in each subject
if len(hypothesis_marks) > len(premise_marks):
    # check if the hypothesis value contradicts the number of marks obtained by the student in each subject
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of marks obtained by the student in each subject
    # any number of marks greater than 'premise_marks' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
