grade_percentile_premise = 90
grade_percentile_hypothesis = 90
total_grades_premise = 80
total_grades_hypothesis = 80

# the hypothesis refers to Angela's grade percentile and total grades mentioned in the premise
if grade_percentile_hypothesis != grade_percentile_premise:
    # check if the grade percentile in the hypothesis contradicts the grade percentile mentioned in the premise
    label = "contradiction"
elif total_grades_hypothesis != total_grades_premise:
    # check if the total grades in the hypothesis contradicts the total grades in the premise
    label = "contradiction"
else:
    # if the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
