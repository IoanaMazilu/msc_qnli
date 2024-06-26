rate_premise = 3.75
rate_hypothesis = 3.75

# the hypothesis and premise mention the interest rate lifted by the Reserve Bank of Australia
if rate_hypothesis!= rate_premise:
    # check if the interest rate in the hypothesis contradicts the interest rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
