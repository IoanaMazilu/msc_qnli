grade_percentile_premise = 80
grade_percentile_hypothesis = 80
total_grades_premise = 120
total_grades_hypothesis = 120

# the hypothesis refers to the percentile of Lena's grade mentioned in the premise
if grade_percentile_hypothesis <= grade_percentile_premise:
    # check if the hypothesis value contradicts the estimate of 'grade_percentile_premise'
    label = "contradiction"
elif grade_percentile_hypothesis > grade_percentile_premise:
    # check if the hypothesis value is greater than 'grade_percentile_premise'
    # this is possible and consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis value is equal to 'grade_percentile_premise', it is a contradiction
    label = "contradiction"

print(label)
