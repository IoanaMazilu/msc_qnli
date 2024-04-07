# Premise: If the agreed period of the debenture was 18 months:calculate the amount of interest Jaclyn will earn for each quarter.
# Hypothesis: If the agreed period of the debenture was less than 38 months:calculate the amount of interest Jaclyn will earn for each quarter.
# Golden Label: entailment

debenture_period_premise = 18
debenture_period_hypothesis = 38

# the hypothesis refers to the debenture period mentioned in the premise
if debenture_period_hypothesis <= debenture_period_premise:
    # check if the hypothesis period contradicts the period in the premise
    label = "contradiction"
elif debenture_period_premise < debenture_period_hypothesis:
    # if the hypothesis period does not contradict the premise period, we can infer entailment
    label = "entailment"
else:
    # if the hypothesis period and premise period are the same, it is neutral
    label = "neutral"

print(label)

