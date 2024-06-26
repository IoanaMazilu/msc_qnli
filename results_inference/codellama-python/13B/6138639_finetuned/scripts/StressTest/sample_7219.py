grade_percentile_premise = 30
grade_percentile_hypothesis = 80

# the hypothesis talks about Lena's grade percentile, referenced also in the premise
if grade_percentile_hypothesis <= grade_percentile_premise:
    # check if the hypothesis value contradicts the estimate of more than 'grade_percentile_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the grade percentile
    # any grade percentile greater than 'grade_percentile_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
