interest_rate_premise = 3.75
hypothesis_interest_rate = 3.75

# the premise and hypothesis mention the same interest rate value
if hypothesis_interest_rate!= interest_rate_premise:
    # check if the interest rate in the hypothesis contradicts the interest rate in the premise
    label = "contradiction"
else:
    # if the interest rate values in the premise and hypothesis are the same, we can infer entailment
    label = "entailment"

print(label)
