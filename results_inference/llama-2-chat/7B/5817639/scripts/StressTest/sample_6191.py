days_premise = 30
days_hypothesis = 45

# the hypothesis talks about the number of days needed to save for a vacation, which is also mentioned in the premise
if days_hypothesis <= days_premise:
    # check if the hypothesis value contradicts the estimate of 'days_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for the number of days needed, but the hypothesis value is greater, so it cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
