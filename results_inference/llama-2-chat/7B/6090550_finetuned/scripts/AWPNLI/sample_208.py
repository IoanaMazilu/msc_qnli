pizzas_ordered = 21.0
slices_per_pizza = 8.0
total_slices = pizzas_ordered * slices_per_pizza

# the hypothesis talks about the total number of slices, which is also referenced in the premise
# compute the total number of slices in the premise
total_slices_premise = pizzas_ordered * slices_per_pizza

if total_slices_premise!= total_slices:
    # check if the total number of slices in the hypothesis contradicts the total number of slices from the premise
    label = "contradiction"
else:
    # if the hypothesis values and the premise values are equal, we can infer entailment
    label = "entailment"

print(label)
