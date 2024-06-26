grade_percentile_premise = 80
grade_percentile_hypothesis = 80
total_grades = 120

# the hypothesis refers to Lena's grade percentile, which is also mentioned in the premise
if grade_percentile_hypothesis <= grade_percentile_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
