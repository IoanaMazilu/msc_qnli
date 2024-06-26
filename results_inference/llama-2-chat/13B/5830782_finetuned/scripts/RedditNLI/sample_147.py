interest_rate_premise = 3.75
interest_rate_hypothesis = 3.75

# the hypothesis and premise mention the interest rate decided by the Reserve Bank of Australia
if interest_rate_premise!= interest_rate_hypothesis:
    # check if the interest rate in the hypothesis contradicts the interest rate in the premise
    label = "contradiction"
else:
    # if the interest rate in the hypothesis does not contradict the interest rate in the premise, we can infer entailment
    label = "entailment"

print(label)
