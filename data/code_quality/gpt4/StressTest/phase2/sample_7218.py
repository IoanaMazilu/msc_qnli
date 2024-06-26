lena_grade_percentile_premise = 80
lena_grade_percentile_hypothesis = 30
total_grades = 120

# the hypothesis refers to the percentile of Lena's grade mentioned in the premise
if lena_grade_percentile_premise <= lena_grade_percentile_hypothesis:
    # check if the estimate of 'lena_grade_percentile_hypothesis' contradicts the number of Lena's grade percentile in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
