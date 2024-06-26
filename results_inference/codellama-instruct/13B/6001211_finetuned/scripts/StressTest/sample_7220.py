grade_percentile_premise = 80
grade_percentile_hypothesis = 80
total_grades = 120

# the hypothesis refers to Lena's grade percentile mentioned in the premise
if grade_percentile_hypothesis <= grade_percentile_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the premise gives the exact grade percentile
    # any percentile greater than 'grade_percentile_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
