investment_premise = 50000
investment_hypothesis = 10000

# the hypothesis talks about the amount of money Mr Sharad invested, referenced also in the premise
if investment_premise <= investment_hypothesis:
    # check if the premise value contradicts the estimate of more than 'investment_hypothesis'
    label = "contradiction"
else:
    # the premise gives the exact amount of money Mr Sharad invested
    # any amount of money greater than 'investment_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "entailment"

print(label)
