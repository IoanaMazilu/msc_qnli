percentile_premise = 30
percentile_hypothesis = 80

# the hypothesis talks about the percentile of Lena's grade, referenced also in the premise
if percentile_hypothesis <= percentile_premise:
    # check if the hypothesis value contradicts the estimate of more than 'percentile_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentile
    # any percentile greater than 'percentile_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
