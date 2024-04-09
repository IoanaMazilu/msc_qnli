percentile_premise = 30
percentile_hypothesis = 80
grades_premise = 120

# the hypothesis refers to the percentile of Lena's grade in her class
if percentile_hypothesis <= percentile_premise:
    # check if the hypothesis value contradicts the estimate of more than 'percentile_premise'
    label = "contradiction"
elif percentile_hypothesis > percentile_premise:
    # the premise gives only an estimate for the percentile of Lena's grade
    # any percentile greater than 'percentile_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
