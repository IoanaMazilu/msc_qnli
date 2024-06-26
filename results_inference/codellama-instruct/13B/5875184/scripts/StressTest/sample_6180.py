premise_marks = [86, 85, 82, 87, 85]
hypothesis_marks = [16, 85, 82, 87, 85]

# the hypothesis refers to the number of marks in each subject, mentioned in the premise
if len(hypothesis_marks) <= len(premise_marks):
    # check if the hypothesis value contradicts the number of marks in each subject in the premise
    label = "contradiction"
elif hypothesis_marks[0] > premise_marks[0]:
    # check if the hypothesis value contradicts the estimate of more than 'premise_marks[0]'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of marks in each subject
    # any number of marks greater than 'premise_marks[0]' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
