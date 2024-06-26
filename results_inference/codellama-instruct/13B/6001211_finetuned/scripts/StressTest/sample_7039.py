average_marks_premise = 26
average_marks_hypothesis = 56

# the hypothesis refers to the average marks of a student in various subjects mentioned in the premise
if average_marks_hypothesis <= average_marks_premise:
    # check if the average marks in the hypothesis contradicts the estimate of more than 'average_marks_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the average marks
    # any average marks greater than 'average_marks_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
