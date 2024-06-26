average_marks_premise = 86
average_marks_hypothesis = 36

# the hypothesis refers to the average marks of Reema mentioned in the premise
if average_marks_hypothesis == average_marks_premise:
    # check if the estimate of 'average_marks_hypothesis' contradicts the average marks in the premise
    label = "contradiction"
else:
    # any number of marks less than 'average_marks_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
