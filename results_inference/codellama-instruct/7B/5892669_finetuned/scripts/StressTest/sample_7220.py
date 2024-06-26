grade_percentile_premise = 80
grade_percentile_hypothesis = 80
total_grades = 120

# the hypothesis refers to Lena's grade percentile mentioned in the premise
if grade_percentile_hypothesis <= grade_percentile_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
