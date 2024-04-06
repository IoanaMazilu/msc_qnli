# Premise: We ordered 21.0 pizzas and each pizza has 8.0 slices.
# Hypothesis: 164.0 slices of pizza are there altogether.
# Golden Label: contradiction

ordered_pizzas_premise = 21.0
slices_each_pizza_premise = 8.0
total_slices_hypothesis = 164.0

# the hypothesis refers to the total number of pizza slices, which can be calculated from the premise
# compute the total number of pizza slices in the premise
total_slices_premise = ordered_pizzas_premise * slices_each_pizza_premise

if total_slices_hypothesis != total_slices_premise:
    # check if the number of pizza slices in the hypothesis contradicts the number of pizza slices from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

