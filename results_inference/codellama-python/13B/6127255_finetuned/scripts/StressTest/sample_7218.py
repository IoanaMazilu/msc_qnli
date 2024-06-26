grade_percentile_premise = 80
grade_percentile_hypothesis = 30
total_grades = 120

# the hypothesis refers to Lena's grade percentile, which is also mentioned in the premise
if grade_percentile_hypothesis >= grade_percentile_premise:
    # check if the grade percentile in the hypothesis contradicts the grade percentile in the premise
    label = "contradiction"
else:
    # if the grade percentile in the hypothesis does not contradict the grade percentile in the premise, we can infer entailment
    label = "entailment"

print(label)
