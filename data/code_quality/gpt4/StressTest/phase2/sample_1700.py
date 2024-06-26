fisherman_hunter_premise = 30
fisherman_hunter_hypothesis = 30
hunter_fisherman_premise = 20
hunter_fisherman_hypothesis = 20

# the hypothesis talks about the percentage of fishermen that are also hunters and the percentage of hunters that are also fishermen
# both are mentioned in the premise
if fisherman_hunter_hypothesis <= fisherman_hunter_premise:
    # check if the hypothesis percentage contradicts the premise value of 'fisherman_hunter_premise'
    label = "contradiction"
elif hunter_fisherman_hypothesis != hunter_fisherman_premise:
    # check if the hypothesis percentage contradicts the premise value of 'hunter_fisherman_premise'
    label = "contradiction"
else:
    # the premise gives exact percentages for both fishermen that are also hunters and hunters that are also fishermen
    # any percentage equal to the premise percentages is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
