# Premise: 4200 from Anwar at 6% p.
# Hypothesis: more than 4200 from Anwar at 6% p.
# Golden Label: contradiction

amount_premise = 4200
amount_hypothesis = 4200
interest_rate_premise = 6
interest_rate_hypothesis = 6

# the hypothesis talks about the amount from Anwar and the interest rate, referenced also in the premise
if amount_hypothesis <= amount_premise:
    # check if the hypothesis value contradicts the estimate of more than 'amount_hypothesis'
    label = "contradiction"
elif interest_rate_hypothesis != interest_rate_premise:
    # check if the interest rate in the hypothesis contradicts the interest rate reported in the premise
    label = "contradiction"
else:
    # the premise gives only an exact amount and interest rate
    # any amount greater than 'amount_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

