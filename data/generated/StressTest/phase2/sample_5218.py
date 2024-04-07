# Premise: Jaclyn buys $less than 80 000 worth of debentures in a company.
# Hypothesis: Jaclyn buys $50 000 worth of debentures in a company.
# Golden Label: neutral

debentures_value_premise = 80000
debentures_value_hypothesis = 50000

# the hypothesis also talks about the amount of debentures bought by Jaclyn, mentioned in the premise
if debentures_value_hypothesis >= debentures_value_premise:
    # check if the value of 'debentures_value_hypothesis' contradicts the upper limit specified in the premise
    label = "contradiction"
else:
    # the premise only specifies an upper limit for the amount of debentures
    # any amount of debentures less than 'debentures_value_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "entailment"

print(label)

