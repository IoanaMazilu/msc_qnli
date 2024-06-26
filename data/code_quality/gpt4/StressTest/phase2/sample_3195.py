investment_premise = 1000
investment_hypothesis = 4000

# the hypothesis is about calculating and comparing the maturity values of a certain amount of money invested in GICs
# which is also mentioned in the premise
if investment_hypothesis <= investment_premise:
    # check if the hypothesized investment contradicts the amount in the premise
    label = "contradiction"
elif investment_hypothesis > investment_premise:
    # the premise gives the exact amount of money invested
    # any amount of money greater than 'investment_premise' is consistent with the premise but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the investment value in the hypothesis does not contradict the investment value in the premise, we can infer entailment
    label = "entailment"

print(label)
