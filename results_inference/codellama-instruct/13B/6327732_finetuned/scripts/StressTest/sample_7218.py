grade_premise = 80
grade_hypothesis = 30

# the hypothesis refers to the percentile of Lena's grade in the class
if grade_hypothesis <= grade_premise:
    # check if the estimate of 'grade_hypothesis' contradicts the percentile of Lena's grade in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentile of Lena's grade
    # any percentile greater than 'grade_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
