pizzas_premise = 21.0
slices_per_pizza_premise = 8.0
total_slices_hypothesis = 168.0

# the hypothesis talks about the total number of slices, which is also referenced in the premise
# compute the total number of slices from the premise
total_slices_premise = pizzas_premise * slices_per_pizza_premise
if total_slices_hypothesis!= total_slices_premise:
    # check if the total number of slices from the hypothesis contradicts the estimate from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
