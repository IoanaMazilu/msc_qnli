deposit_premise = 1000000
deposit_hypothesis = 2000000
interest_rate_premise = 4
interest_rate_hypothesis = 4

# the hypothesis talks about the amount deposited by Alice and the interest rate, both mentioned in the premise
if deposit_hypothesis <= deposit_premise:
    # check if the hypothesis value contradicts the premise estimate of more than 'deposit_premise'
    label = "contradiction"
elif interest_rate_hypothesis != interest_rate_premise:
    # check if the interest rate in the hypothesis contradicts the interest rate reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount deposited
    # any amount greater than 'deposit_premise' is consistent with the premise, but cannot be explicitly entailed from it
    label = "neutral"

print(label)
