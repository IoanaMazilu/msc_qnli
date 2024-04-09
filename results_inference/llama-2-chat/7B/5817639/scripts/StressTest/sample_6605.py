original_investment_premise = 2
original_investment_hypothesis = 1

# the hypothesis talks about the return on investment, which is also mentioned in the premise
if original_investment_hypothesis <= original_investment_premise:
    # check if the hypothesis value contradicts the estimate of 'original_investment_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for the return on investment, which cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
