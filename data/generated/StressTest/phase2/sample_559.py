# Premise: Jaclyn buys $less than 80 000 worth of debentures in a company.
# Hypothesis: Jaclyn buys $20 000 worth of debentures in a company.
# Golden Label: neutral

debentures_premise = 80000
debentures_hypothesis = 20000

# the hypothesis talks about the worth of debentures Jaclyn buys, which is also referenced in the premise
if debentures_hypothesis >= debentures_premise:
    # check if the hypothesis value contradicts the estimate of 'less than debentures_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the worth of debentures
    # any worth of debentures less than 'debentures_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

