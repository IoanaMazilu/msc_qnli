amount_premise = 3600
amount_hypothesis = 3600
interest_rate_premise = 6
interest_rate_hypothesis = 6

# the hypothesis refers to the amount from Anwar and the interest rate mentioned in the premise
if amount_hypothesis <= amount_premise:
    # check if the estimate of 'amount_hypothesis' contradicts the amount in the premise
    label = "contradiction"
elif interest_rate_hypothesis!= interest_rate_premise:
    # check if the interest rate in the hypothesis contradicts the interest rate reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
