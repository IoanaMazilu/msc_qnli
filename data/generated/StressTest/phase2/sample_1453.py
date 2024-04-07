# Premise: Jaclyn buys $more than 10 000 worth of debentures in a company.
# Hypothesis: Jaclyn buys $40 000 worth of debentures in a company.
# Golden Label: neutral

debentures_premise = 10000
debentures_hypothesis = 40000

# the hypothesis talks about the value of debentures bought by Jaclyn, referenced also in the premise
if debentures_hypothesis <= debentures_premise:
    # check if the hypothesis value contradicts the estimate of more than 'debentures_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the value of debentures
    # any value of debentures greater than 'debentures_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

