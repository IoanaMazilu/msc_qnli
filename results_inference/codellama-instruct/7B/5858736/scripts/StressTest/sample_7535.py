# Define variables for the numerical entities in the premise and hypothesis
premise_leo_weight = 10
premise_sister_weight = 80
hypothesis_leo_weight = 80
hypothesis_sister_weight = 10

# Calculate the difference in weight between Leo and his sister
leo_weight_diff = hypothesis_leo_weight - premise_leo_weight
sister_weight_diff = hypothesis_sister_weight - premise_sister_weight

# Check if the difference in weight between Leo and his sister contradicts the premise
if leo_weight_diff!= sister_weight_diff:
    label = "contradiction"
else:
    # If the difference in weight between Leo and his sister does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
