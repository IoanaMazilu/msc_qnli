earnings_premise = 79800
earnings_hypothesis = 19800

# the hypothesis talks about the earnings of Shridhar, which is also mentioned in the premise
if earnings_hypothesis >= earnings_premise:
    # check if the earnings in the hypothesis contradict the estimate of less than 'earnings_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the earnings
    # any earnings less than 'earnings_premise' is consistent with the premise, 
    # but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
