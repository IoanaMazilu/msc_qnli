interest_rate_premise = 3.75
interest_rate_hypothesis = 3.75

# the hypothesis and premise mention the interest rates after an increase in Australia
if interest_rate_hypothesis != interest_rate_premise:
    # check if the interest rate in the hypothesis contradicts the interest rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
