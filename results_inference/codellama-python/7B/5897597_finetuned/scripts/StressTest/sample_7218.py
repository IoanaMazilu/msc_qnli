grade_percentile_premise = 80
grade_percentile_hypothesis = 30
total_grades = 120

# the hypothesis refers to Lena's grade percentile mentioned in the premise
if grade_percentile_premise <= grade_percentile_hypothesis:
    # check if the estimate of 'grade_percentile_hypothesis' contradicts the grade percentile in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
