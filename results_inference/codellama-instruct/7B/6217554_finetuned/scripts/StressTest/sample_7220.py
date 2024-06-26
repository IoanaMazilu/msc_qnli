grade_percentile_premise = 80
grade_percentile_hypothesis = 80
total_grades_premise = 120
total_grades_hypothesis = 120

# the hypothesis refers to the grade percentile and total number of grades mentioned in the premise
if grade_percentile_hypothesis >= grade_percentile_premise:
    # check if the hypothesis value contradicts the grade percentile in the premise
    label = "contradiction"
elif total_grades_hypothesis!= total_grades_premise:
    # check if the total number of grades in the hypothesis contradicts the total number of grades reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
