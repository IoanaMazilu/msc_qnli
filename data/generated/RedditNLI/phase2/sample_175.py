# Premise: BofA sets aside $14bn to cover loan claims-FT.com.
# Hypothesis: BofA sets aside $14 bn for U.S. mortgage claims.
# Golden Label: neutral

amount_set_aside_premise = 14
amount_set_aside_hypothesis = 14

# the hypothesis and premise mention the amount BofA sets aside
if amount_set_aside_hypothesis != amount_set_aside_premise:
    # check if the amount set aside in the hypothesis contradicts the amount set aside in the premise
    label = "contradiction"
else:
    # if the amount set aside does not contradict, it does not necessarily entail the specifics of the claims (loan vs. mortgage)
    label = "neutral"

print(label)

