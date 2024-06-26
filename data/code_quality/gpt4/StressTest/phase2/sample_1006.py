investment_premise = 15000
investment_hypothesis = 55000

# the hypothesis talks about the amount Mitra invested, which is also mentioned in the premise
if investment_hypothesis <= investment_premise:
    # check if the hypothesis value contradicts the estimate of more than 'investment_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the investment
    # any investment greater than 'investment_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
