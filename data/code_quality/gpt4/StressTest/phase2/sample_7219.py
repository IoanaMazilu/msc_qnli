percentile_premise = 30
percentile_hypothesis = 80
total_grades = 120

# The hypothesis talks about Lena's percentile in her class, which is also referenced in the premise
if percentile_hypothesis <= percentile_premise:
    # check if the hypothesis value contradicts the estimate of more than 'percentile_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for Lena's percentile
    # any percentile greater than 'percentile_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
