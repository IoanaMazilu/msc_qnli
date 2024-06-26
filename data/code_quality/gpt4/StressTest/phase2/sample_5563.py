earnings_increase_premise = 87
earnings_increase_hypothesis = 27
earnings_premise = 567
earnings_hypothesis = 567

# the hypothesis talks about Albert’s monthly earnings, referenced also in the premise
if earnings_increase_hypothesis >= earnings_increase_premise:
    # check if the hypothesis value contradicts the estimate of less than 'earnings_increase_premise'
    label = "contradiction"
elif earnings_hypothesis != earnings_premise:
    # check if the earnings value in the hypothesis contradicts the earnings value reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage increase of earnings
    # any percentage increase less than 'earnings_increase_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
