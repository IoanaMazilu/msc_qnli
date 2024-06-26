deposit_premise = 22500
deposit_hypothesis = 62500
interest_rate_premise = 8
interest_rate_hypothesis = 8
compounding_period_premise = 4
compounding_period_hypothesis = 4

# the hypothesis refers to the deposit amount and interest rate mentioned in the premise
if deposit_hypothesis <= deposit_premise:
    # check if the hypothesis value contradicts the estimate of more than 'deposit_premise'
    label = "contradiction"
elif interest_rate_hypothesis!= interest_rate_premise:
    # check if the interest rate in the hypothesis contradicts the interest rate reported in the premise
    label = "contradiction"
elif compounding_period_hypothesis!= compounding_period_premise:
    # check if the compounding period in the hypothesis contradicts the compounding period reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
