# Premise: If the agreed period of the debenture was 18 months:calculate the amount of interest Jaclyn will earn for each quarter.
# Hypothesis: If the agreed period of the debenture was less than 18 months:calculate the amount of interest Jaclyn will earn for each quarter.
# Golden Label: contradiction

debenture_period_premise = 18
debenture_period_hypothesis = 18

# the hypothesis refers to the period of the debenture mentioned in the premise
if debenture_period_hypothesis >= debenture_period_premise:
    # check if the hypothesis contradicts the estimate of 'debenture_period_hypothesis' being less than the debenture period in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

