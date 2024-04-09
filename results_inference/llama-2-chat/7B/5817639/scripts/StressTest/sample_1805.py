compound_interest_premise = 8
compound_interest_hypothesis = 4

# the hypothesis talks about the compound interest rate, which is also referred to in the premise
if compound_interest_hypothesis <= compound_interest_premise:
    # check if the hypothesis value contradicts the estimate of the compound interest rate in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the compound interest rate, and any lower rate than that is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
