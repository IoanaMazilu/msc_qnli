# Premise: Jaclyn buys $30 000 worth of debentures in a company.
# Hypothesis: Jaclyn buys $20 000 worth of debentures in a company.
# Golden Label: contradiction

debentures_bought_premise = 30000
debentures_bought_hypothesis = 20000

# the hypothesis references the amount of debentures bought by Jaclyn, also mentioned in the premise
if debentures_bought_hypothesis != debentures_bought_premise:
    # check if the amount of debentures bought in the hypothesis contradicts the amount of debentures bought reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

