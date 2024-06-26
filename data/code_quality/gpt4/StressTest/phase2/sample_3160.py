investment_return_premise = 3
investment_return_hypothesis = 5

# the hypothesis talks about the return on investment after 'n' years, referenced also in the premise
if investment_return_hypothesis <= investment_return_premise:
    # check if the hypothesis value contradicts the estimate of more than 'investment_return_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the return on investment
    # any return on investment greater than 'investment_return_premise' is consistent with the premise, but cannot be explicitly inferred from the premise
    label = "neutral"

print(label)
