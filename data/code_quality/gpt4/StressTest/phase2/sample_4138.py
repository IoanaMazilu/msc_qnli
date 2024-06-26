investment_return_premise = 4
investment_return_hypothesis = 7

# the hypothesis talks about the return of investment Sandy got back, referenced also in the premise
if investment_return_hypothesis <= investment_return_premise:
    # check if the hypothesis value contradicts the estimate of more than 'investment_return_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the return of investment
    # any return of investment greater than 'investment_return_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
