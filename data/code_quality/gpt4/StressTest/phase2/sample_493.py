average_grade_premise = 29
average_grade_hypothesis = 79

# the hypothesis talks about Alice's average grade, referenced also in the premise
if average_grade_hypothesis <= average_grade_premise:
    # check if the hypothesis value contradicts the estimate of more than 'average_grade_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the average grade
    # any average grade greater than 'average_grade_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
