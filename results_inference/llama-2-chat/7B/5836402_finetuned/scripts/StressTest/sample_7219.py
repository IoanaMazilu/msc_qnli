percentile_grade_premise = 30
percentile_grade_hypothesis = 80
total_grades_premise = 120
total_grades_hypothesis = 120

# the hypothesis talks about Lena's grade percentile, which is also referenced in the premise
if percentile_grade_hypothesis <= percentile_grade_premise:
    # check if the hypothesis value contradicts the estimate of more than 'percentile_grade_premise'
    label = "contradiction"
elif percentile_grade_hypothesis > percentile_grade_premise:
    # the premise gives only an estimate for the grade percentile
    # any percentile greater than 'percentile_grade_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis value and the premise estimate match, we can infer entailment
    label = "entailment"

print(label)
