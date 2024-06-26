# Define variables for the premise
area_ratio_premise = 144
area_trapezium_premise = 25
base_trapezium_premise = 13

# Define variables for the hypothesis
area_ratio_hypothesis = 244
area_trapezium_hypothesis = 25
base_trapezium_hypothesis = 13

# Check if the hypothesis values and estimates do not contradict the premise ones
if area_ratio_hypothesis <= area_ratio_premise and base_trapezium_hypothesis <= base_trapezium_premise:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"
else:
    # If the hypothesis values and estimates contradict the premise ones, we can infer contradiction
    label = "contradiction"

print(label)
