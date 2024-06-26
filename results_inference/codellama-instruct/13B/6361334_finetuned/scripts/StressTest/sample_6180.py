marks_premise = [86, 85, 82, 87, 85]
marks_hypothesis = [16, 85, 82, 87, 85]

# the hypothesis refers to the number of marks obtained in each subject, which is also mentioned in the premise
if len(marks_hypothesis) <= len(marks_premise):
    # check if the hypothesis value contradicts the number of marks in each subject in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of marks in each subject
    # any number of marks greater than the premise ones is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
