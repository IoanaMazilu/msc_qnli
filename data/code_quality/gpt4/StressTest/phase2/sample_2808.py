average_marks_premise = 15
average_marks_hypothesis = 65

# the hypothesis talks about the average marks scored by Ganesh in certain subjects, referenced also in the premise
if average_marks_hypothesis < average_marks_premise:
    # check if the hypothesis value contradicts the estimate of less than 'average_marks_premise'
    label = "contradiction"
elif average_marks_hypothesis == average_marks_premise:
    # check if the hypothesis value is exactly the same as 'average_marks_premise'
    label = "entailment"
else:
    # the premise gives only an estimate for the average marks
    # any average marks greater than 'average_marks_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
