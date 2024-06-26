average_marks_premise = 56
average_marks_hypothesis = 26

# the hypothesis talks about the number of marks obtained in specific subjects
if average_marks_hypothesis <= average_marks_premise:
    # check if the hypothesis value contradicts the estimate of more than 'average_marks_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of marks obtained in specific subjects
    # any number of marks obtained in those subjects greater than 'average_marks_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
