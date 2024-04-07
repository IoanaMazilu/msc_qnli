# Premise: Jaclyn buys $40 000 worth of debentures in a company.
# Hypothesis: Jaclyn buys $30 000 worth of debentures in a company.
# Golden Label: contradiction

debentures_premise = 40000
debentures_hypothesis = 30000

# The hypothesis makes a statement about the amount of debentures Jaclyn buys, which is also mentioned in the premise
if debentures_premise == debentures_hypothesis:
    # Check if the amount of debentures in the hypothesis is the same as what is stated in the premise
    label = "entailment"
elif debentures_premise < debentures_hypothesis:
    # Check if the amount of debentures in the hypothesis contradicts what is stated in the premise
    label = "contradiction"
else:
    # If the amount of debentures in the hypothesis is less than the premise, it doesn't contradict but also cannot be fully entailed
    label = "neutral"

print(label)

