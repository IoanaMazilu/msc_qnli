grade_percentile_premise = 30
grade_percentile_hypothesis = 80
total_grades = 120

# the hypothesis refers to Lena's grade percentile, which is also mentioned in the premise
if grade_percentile_hypothesis <= grade_percentile_premise:
    # check if the hypothesis grade percentile contradicts the premise estimate of more than 'grade_percentile_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the grade percentile
    # any grade percentile greater than 'grade_percentile_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
