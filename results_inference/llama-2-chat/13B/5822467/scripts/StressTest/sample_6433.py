premise_investment = 5000
hypothesis_investment = 8000
interest_rate = 5

# the hypothesis refers to the amount invested and the interest rate mentioned in the premise
if hypothesis_investment > premise_investment:
    # check if the estimate of 'hypothesis_investment' contradicts the amount invested in the premise
    label = "contradiction"
elif hypothesis_investment == premise_investment:
    # the premise gives only an estimate for the amount invested
    # the hypothesis value is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # the hypothesis value is greater than the premise value, and the interest rate is the same
    # we can infer entailment
    label = "entailment"

print(label)
