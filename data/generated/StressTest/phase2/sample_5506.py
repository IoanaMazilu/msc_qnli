# Premise: Jaclyn buys $less than 80 000 worth of debentures in a company.
# Hypothesis: Jaclyn buys $10 000 worth of debentures in a company.
# Golden Label: neutral

debentures_premise = 80000
debentures_hypothesis = 10000

# the hypothesis refers to the amount spent on buying debentures, also mentioned in the premise
if debentures_hypothesis >= debentures_premise:
    # check if the hypothesis value contradicts the estimate of less than 'debentures_premise'
    label = "contradiction"
elif debentures_hypothesis < debentures_premise:
    # any amount less than 'debentures_premise' is consistent with the premise and can be explicitly entailed from the premise
    label = "entailment"

print(label)

