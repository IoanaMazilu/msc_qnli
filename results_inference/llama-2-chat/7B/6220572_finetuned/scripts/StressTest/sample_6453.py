average_marks_premise = [66, 60, 72, 77, 55, 85]
average_marks_hypothesis = [76, 60, 72, 77, 55, 85]

# the hypothesis refers to the scores and the average mark calculation in the premise
if any(average_marks_hypothesis[i] >= average_marks_premise[i] for i in range(len(average_marks_premise))):
    # check if the hypothesis values contradict the average marks calculated in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the average mark
    # any average mark less than 'average_marks_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
