# Premise: If the agreed period of the debenture was 18 months:calculate the amount of interest Jaclyn will earn for each quarter.
# Hypothesis: If the agreed period of the debenture was less than 68 months:calculate the amount of interest Jaclyn will earn for each quarter.
# Golden Label: entailment

debenture_period_premise = 18
debenture_period_hypothesis = 68

# the hypothesis refers to the period of the debenture mentioned in the premise
if debenture_period_hypothesis < debenture_period_premise:
    # check if the hypothesis value contradicts the debenture period mentioned in the premise
    label = "contradiction"
elif debenture_period_hypothesis > debenture_period_premise:
    # the hypothesis gives an estimate for the debenture period
    # any period less than 'debenture_period_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

