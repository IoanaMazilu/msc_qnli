# Premise: Lucy deposited $more than 22500 in an investment fund that provided 8 percent annual return compounded quarterly.
# Hypothesis: Lucy deposited $62500 in an investment fund that provided 8 percent annual return compounded quarterly.
# Golden Label: neutral

deposit_premise = 22500
deposit_hypothesis = 62500
annual_return = 0.08  # as it is 8 percent

# the hypothesis talks about the amount Lucy deposited in the investment fund, which is also referenced in the premise
if deposit_hypothesis <= deposit_premise:
    # check if the hypothesis value contradicts the estimate of more than 'deposit_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the deposit
    # any deposited amount greater than 'deposit_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

