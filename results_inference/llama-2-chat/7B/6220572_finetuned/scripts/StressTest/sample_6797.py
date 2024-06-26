deposit_premise = 62500
deposit_hypothesis = 62500
interest_rate_premise = 8
interest_rate_hypothesis = 8

# the hypothesis talks about the deposit amount and interest rate mentioned in the premise
if deposit_hypothesis >= deposit_premise:
    # check if the hypothesis value contradicts the estimate of less than 'deposit_premise'
    label = "contradiction"
elif interest_rate_hypothesis!= interest_rate_premise:
    # check if the interest rate in the hypothesis contradicts the interest rate reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
