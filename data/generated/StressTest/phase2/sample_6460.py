# Premise: Lucy deposited $less than 72500 in an investment fund that provided 20 percent annual return compounded quarterly.
# Hypothesis: Lucy deposited $62500 in an investment fund that provided 20 percent annual return compounded quarterly.
# Golden Label: neutral

deposit_premise = 72500
deposit_hypothesis = 62500
return_rate = 20

# the hypothesis talks about the amount of money Lucy deposited in an investment fund
# which is also mentioned in the premise
if deposit_hypothesis >= deposit_premise:
    # check if the deposit value in the hypothesis contradicts the premise that Lucy deposited less than deposit_premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the deposit amount
    # any deposit amount less than deposit_premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

