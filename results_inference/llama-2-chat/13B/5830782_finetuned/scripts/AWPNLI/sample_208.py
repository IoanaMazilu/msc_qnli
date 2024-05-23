pizzas_ordered_premise = 21.0
slices_per_pizza_premise = 8.0
total_slices_hypothesis = 168.0

# the hypothesis refers to the total number of pizza slices, which are also mentioned in the premise
# compute the total number of pizza slices in the premise
total_slices_premise = pizzas_ordered_premise * slices_per_pizza_premise
if total_slices_hypothesis!= total_slices_premise:
    # check if the total number of pizza slices in the hypothesis contradicts the total number of pizza slices from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)