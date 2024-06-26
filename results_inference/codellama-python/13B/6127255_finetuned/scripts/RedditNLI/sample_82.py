investment_premise = 1
investment_hypothesis = 1

# the hypothesis and premise mention the amount of investment in US by General Motors
if investment_hypothesis < investment_premise:
    # check if the amount of investment in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # the premise gives an exact amount of investment
    # any amount of investment in the hypothesis equal or greater than 'investment_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "entailment"

print(label)
