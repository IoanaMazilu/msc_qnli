grade_premise = 80
grade_hypothesis = 85

# the hypothesis talks about the percentile of Lena's grade, referenced also in the premise
if grade_hypothesis <= grade_premise:
    # check if the hypothesis value contradicts the estimate of more than 'grade_premise' percentile
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentile of Lena's grade
    # any percentile greater than 'grade_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
