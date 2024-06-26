labels = ["entailment", "contradiction", "neutral"]

# Define variables for premise and hypothesis
premise_tree_explosives = 2
hypothesis_tree_explosives = 2

# Check if the hypothesis contradicts the premise
if hypothesis_tree_explosives!= premise_tree_explosives:
    label = "contradiction"
else:
    # If the values are the same, we can infer entailment
    label = "entailment"

print(label)
