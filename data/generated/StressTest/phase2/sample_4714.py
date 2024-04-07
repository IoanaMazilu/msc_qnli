# Premise: Jaclyn buys $less than 40 000 worth of debentures in a company.
# Hypothesis: Jaclyn buys $30 000 worth of debentures in a company.
# Golden Label: neutral

debt_premise = 40000
debt_hypothesis = 30000

# the hypothesis talks about the value of debentures bought by Jaclyn, also referenced in the premise
if debt_hypothesis >= debt_premise:
    # check if the hypothesis value contradicts the estimate of less than 'debt_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the value of the debentures
    # any value of debentures less than 'debt_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

