original_investment_premise = 2 * 100 = 200
original_investment_hypothesis = 3 * 100 = 300

# the hypothesis talks about the return on investment, which is also referenced in the premise
if original_investment_hypothesis <= original_investment_premise:
    # check if the hypothesis value contradicts the estimate of 'original_investment_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the return on investment
    # any return less than 'original_investment_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
