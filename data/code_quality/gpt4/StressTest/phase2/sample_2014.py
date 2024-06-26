loan_period_premise = 6
loan_period_hypothesis = 2
interest_rate_premise = 4
interest_rate_hypothesis = 4

# The hypothesis talks about the potential losses Indu would have suffered if she loaned to Bindu for a certain period at a certain interest rate. 
# These quantities are also mentioned in the premise.

if loan_period_hypothesis >= loan_period_premise:
    # Check if the loan period in the hypothesis contradicts the premise's loan period
    label = "contradiction"
elif interest_rate_hypothesis != interest_rate_premise:
    # Check if the interest rate in the hypothesis contradicts the premise's interest rate
    label = "contradiction"
else:
    # The premise gives an estimate for the loan period and the interest rate.
    # Any loan period less than 'loan_period_premise' at an interest rate equal to 'interest_rate_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
