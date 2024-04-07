# Premise: Lucy deposited $more than 27600 in an investment fund that provided 16 percent annual return compounded quarterly.
# Hypothesis: Lucy deposited $67600 in an investment fund that provided 16 percent annual return compounded quarterly.
# Golden Label: neutral

deposit_premise = 27600
deposit_hypothesis = 67600
return_rate_premise = 16
return_rate_hypothesis = 16

# the hypothesis makes a claim about the deposit amount and the return rate, both referenced in the premise
if deposit_hypothesis <= deposit_premise:
    # check if the deposit amount in the hypothesis contradicts the estimate of more than 'deposit_premise' in the premise
    label = "contradiction"
elif return_rate_hypothesis != return_rate_premise:
    # check if the return rate in the hypothesis contradicts the return rate reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the deposit amount
    # any deposit amount greater than 'deposit_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

