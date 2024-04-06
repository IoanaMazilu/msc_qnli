# Premise: World Bank:'extreme poverty' to fall below 10% of world population for first time.
# Hypothesis: World poverty to drop below 10% for first time; Capitalism to blame.
# Golden Label: neutral

poverty_rate_premise = 10
poverty_rate_hypothesis = 10

# the hypothesis and premise mention the same poverty rate
# the statement about capitalism in the hypothesis cannot be inferred from the premise
if poverty_rate_premise != poverty_rate_hypothesis:
    # check if the poverty rate in the hypothesis contradicts the poverty rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we infer neutrality
    # because the attribution to capitalism cannot be entailed from the premise
    label = "neutral"

print(label)

