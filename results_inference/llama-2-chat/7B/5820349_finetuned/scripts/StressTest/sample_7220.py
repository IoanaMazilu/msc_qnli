percentile_grade_premise = 80
percentile_grade_hypothesis = 80
total_grades = 120

# the hypothesis refers to Lena's grade percentile mentioned in the premise
if percentile_grade_hypothesis >= percentile_grade_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise value, it does not contradict the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
