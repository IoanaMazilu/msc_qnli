average_marks_difference_premise = 65
average_marks_difference_hypothesis = 15

# the hypothesis talks about the average marks difference in certain subjects, also referred in the premise
if average_marks_difference_hypothesis >= average_marks_difference_premise:
    # check if the hypothesis value contradicts the estimate of less than 'average_marks_difference_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the difference of average marks
    # any difference less than 'average_marks_difference_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
