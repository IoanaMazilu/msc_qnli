interest_rate_premise = 6
interest_rate_hypothesis = 8

# the hypothesis refers to the interest rate at which Nitin borrowed some money, mentioned in the premise
if interest_rate_hypothesis!= interest_rate_premise:
    # check if the interest rate in the hypothesis contradicts the interest rate reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
