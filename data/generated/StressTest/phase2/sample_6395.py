# Premise: George's car calls for 8 ounces of oil for each cylinder used.
# Hypothesis: George's car calls for more than 8 ounces of oil for each cylinder used.
# Golden Label: contradiction

oil_per_cylinder_premise = 8
oil_per_cylinder_hypothesis = 8

# the hypothesis refers to the amount of oil per cylinder mentioned in the premise
if oil_per_cylinder_hypothesis > oil_per_cylinder_premise:
    # check if the estimate of 'oil_per_cylinder_hypothesis' contradicts the amount of oil per cylinder in the premise
    label = "contradiction"
elif oil_per_cylinder_hypothesis <= oil_per_cylinder_premise:
    # check if the amount of oil per cylinder in the hypothesis contradicts the amount of oil per cylinder reported in the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)

