# Premise: Can the BAT, which stands for buoyant airborne turbine, help bring life-saving electricity to an estimated 1 billion people in rural areas where power is unavailable?
# Hypothesis: Worldwide, an estimated 1 billion rural residents have no access to electricity.
# Golden Label: neutral

people_without_power_premise = 1000000000
people_without_power_hypothesis = 1000000000

# the hypothesis mentions the number of people worldwide without access to electricity, which is also referenced in the premise
if people_without_power_hypothesis != people_without_power_premise:
    # check if the number of people without power in the hypothesis contradicts the number of people without power reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)

