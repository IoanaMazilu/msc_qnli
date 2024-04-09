jill_earnings_premise = 6.00
jill_earnings_hypothesis = 6.00
tip_rate_premise = 0.75
tip_rate_hypothesis = 0.35

# the hypothesis refers to the tip rate of Jill in the premise
if jill_earnings_hypothesis <= jill_earnings_premise:
    # check if the hypothesis value contradicts the estimate of the hourly wage in the premise
    label = "contradiction"
elif tip_rate_hypothesis!= tip_rate_premise:
    # check if the hypothesis tip rate contradicts the estimate of the tip rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
