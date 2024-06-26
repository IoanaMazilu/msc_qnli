# Define variables for the premise and hypothesis
premise_x = 7
premise_y = 7
premise_z = 7
hypothesis_x = 3
hypothesis_y = 3
hypothesis_z = 3

# Check if the hypothesis values are consistent with the premise
if hypothesis_x * hypothesis_y * hypothesis_z == premise_x * premise_y * premise_z:
    # The hypothesis values are consistent with the premise, so we can infer entailment
    label = "entailment"
else:
    # The hypothesis values are not consistent with the premise, so we can infer contradiction
    label = "contradiction"

print(label)
