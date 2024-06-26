interest_rate_premise = 8
interest_rate_hypothesis = 8

# the hypothesis refers to the interest rate mentioned in the premise
if interest_rate_hypothesis >= interest_rate_premise:
    # check if the estimate of 'interest_rate_hypothesis' contradicts the interest rate in the premise
    label = "contradiction"
else:
    # if the hypothesis interest rate does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
