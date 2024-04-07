# Premise: Jaclyn buys $20 000 worth of debentures in a company.
# Hypothesis: Jaclyn buys $less than 20 000 worth of debentures in a company.
# Golden Label: contradiction

debentures_premise = 20000
debentures_hypothesis = 20000

# the hypothesis refers to the amount of debentures bought by Jaclyn, which is also mentioned in the premise
if debentures_hypothesis >= debentures_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise, it does not contradict the premise
    # but it cannot be explicitly entailed from the premise either
    label = "neutral"

print(label)

