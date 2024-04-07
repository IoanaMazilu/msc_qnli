# Premise: If the agreed period of the debenture was 18 months:calculate the amount of interest Jaclyn will earn for each quarter.
# Hypothesis: If the agreed period of the debenture was 68 months:calculate the amount of interest Jaclyn will earn for each quarter.
# Golden Label: contradiction

debenture_period_premise = 18
debenture_period_hypothesis = 68

# The hypothesis refers to the period of the debenture mentioned in the premise
if debenture_period_premise != debenture_period_hypothesis:
    # Check if the debenture period in the hypothesis contradicts the debenture period in the premise
    label = "contradiction"
else:
    # If the debenture period in the hypothesis does not contradict the debenture period in the premise, we can infer entailment
    label = "entailment"

print(label)

