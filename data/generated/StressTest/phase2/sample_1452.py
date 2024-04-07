# Premise: Jaclyn buys $40 000 worth of debentures in a company.
# Hypothesis: Jaclyn buys $more than 10 000 worth of debentures in a company.
# Golden Label: entailment

debentures_premise = 40000
debentures_hypothesis = 10000

# the hypothesis refers to the amount of debentures bought by Jaclyn, which is also mentioned in the premise
if debentures_premise <= debentures_hypothesis:
    # check if the hypothesis value contradicts the estimate of 'debentures_premise'
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise value, we can infer entailment
    label = "entailment"

print(label)

