coffee_weight_premise = 85
coffee_weight_hypothesis = 75

# The hypothesis talks about the total weight of coffee that Carina has, which is referenced in the premise
if coffee_weight_hypothesis != coffee_weight_premise:
    # Check if the total weight of coffee in the hypothesis contradicts the total weight of coffee mentioned in the premise
    label = "contradiction"
else:
    # If the total weight of coffee in the hypothesis is equal to the total weight of coffee in the premise, we can infer entailment
    label = "entailment"

print(label)
