interest_rate_premise = 3.75
interest_rate_hypothesis = 3.75

# The hypothesis mentions the interest rate in Australia, which is also mentioned in the premise
if interest_rate_hypothesis!= interest_rate_premise:
    # If the interest rate in the hypothesis is not the same as in the premise, we can infer entailment
    label = "entailment"
else:
    # If the interest rates are the same, we can infer contradiction
    label = "contradiction"

print(label)
