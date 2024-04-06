# Premise: We ordered 21.0 pizzas and each pizza has 8.0 slices.
# Hypothesis: 168.0 slices of pizza are there altogether.
# Golden Label: entailment

ordered_pizzas_premise = 21.0
slices_per_pizza_premise = 8.0
total_slices_hypothesis = 168.0

# the hypothesis refers to the total number of slices, which can be computed from the premise
# calculate the total number of slices in the premise
total_slices_premise = ordered_pizzas_premise * slices_per_pizza_premise
if total_slices_hypothesis != total_slices_premise:
    # check if the total number of slices in the hypothesis contradicts the total number of slices from the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)

