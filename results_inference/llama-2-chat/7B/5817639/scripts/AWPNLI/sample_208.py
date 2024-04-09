ordered_pizzas_premise = 21.0
slices_per_pizza_premise = 8.0
total_slices_premise = ordered_pizzas_premise * slices_per_pizza_premise
hypothetical_slices = 168.0

# The hypothesis talks about the total number of slices of pizza, which is also mentioned in the premise
# Compute the total number of slices in the premise
total_slices_hypothesis = ordered_pizzas_premise * slices_per_pizza_premise

# Check if the number of slices in the hypothesis contradicts the number of slices in the premise
if total_slices_hypothesis!= total_slices_premise:
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
