original_investment_premise = 3
original_investment_hypothesis = 2

# the hypothesis talks about the original investment, which is also referenced in the premise
if original_investment_hypothesis < original_investment_premise:
    # check if the hypothesis value contradicts the estimate of less than 'original_investment_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the original investment
    # any original investment greater than 'original_investment_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
