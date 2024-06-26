amount_premise = 3600
amount_hypothesis = 3600
interest_rate_premise = 6
interest_rate_hypothesis = 6

# the hypothesis talks about the same amount and interest rate as the premise
if amount_hypothesis!= amount_premise:
    # check if the amount in the hypothesis contradicts the amount in the premise
    label = "contradiction"
elif interest_rate_hypothesis!= interest_rate_premise:
    # check if the interest rate in the hypothesis contradicts the interest rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
