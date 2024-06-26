rate_growth_premise = 2.5
rate_growth_hypothesis = 0.0

# the hypothesis and premise mention the growth rate of the US economy
if rate_growth_hypothesis < rate_growth_premise:
    # check if the growth rate in the hypothesis contradicts the growth rate in the premise
    label = "contradiction"
elif rate_growth_hypothesis > rate_growth_premise:
    # check if the growth rate in the hypothesis contradicts the growth rate in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the growth rate
    # any estimate of the growth rate in the hypothesis greater or equal to 'rate_growth_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
