percentile_premise = 80
percentile_hypothesis = 30

# the hypothesis refers to the percentile of Lena's grade mentioned in the premise
if percentile_hypothesis >= percentile_premise:
    # check if the estimate of 'percentile_hypothesis' contradicts the percentile of Lena's grade in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentile of Lena's grade
    # any percentile greater than 'percentile_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
