interest_rate_premise = 8
interest_rate_hypothesis = 7

# the hypothesis refers to the interest rate mentioned in the premise
if interest_rate_premise >= interest_rate_hypothesis:
    # check if the interest rate in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
