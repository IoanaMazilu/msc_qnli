earnings_premise = 600
earnings_hypothesis = 700

# the hypothesis and premise mention the earnings of Schwartzman 
if earnings_hypothesis < earnings_premise:
    # check if the earnings in the hypothesis contradict the earnings in the premise
    label = "contradiction"
elif earnings_hypothesis > earnings_premise:
    # the premise gives only an estimate for the earnings
    # any estimate of the earnings in the hypothesis greater than 'earnings_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
