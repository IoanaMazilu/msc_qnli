# Premise: 300 tax added to Harini's pet cost.
# Hypothesis: more than 100 tax added to Harini's pet cost.
# Golden Label: entailment

tax_premise = 300
tax_hypothesis = 100

# the hypothesis refers to the tax amount mentioned in the premise
if tax_premise > tax_hypothesis:
    # if the known tax in the premise is greater than the tax in the hypothesis, we can infer entailment
    label = "entailment"
elif tax_premise <= tax_hypothesis:
    # check if the estimate of 'tax_hypothesis' contradicts the tax amount in the premise
    label = "contradiction"
else:
    # if the hypothesis value and estimate do not contradict the premise ones, but cannot fully entail either
    label = "neutral"

print(label)

