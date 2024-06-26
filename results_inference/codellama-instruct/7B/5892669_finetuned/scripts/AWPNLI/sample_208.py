ordered_pizzas_premise = 21.0
slices_per_pizza_premise = 8.0
total_slices_hypothesis = 168.0

# the hypothesis refers to the total number of pizza slices, which can be computed from the premise
# compute the total number of pizza slices in the premise
total_slices_premise = ordered_pizzas_premise * slices_per_pizza_premise
if total_slices_hypothesis!= total_slices_premise:
    # check if the total number of slices in the hypothesis contradicts the total number of slices from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
