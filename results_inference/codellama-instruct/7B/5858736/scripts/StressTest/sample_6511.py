# Define variables for the premise and hypothesis
premise_x = 1
premise_y = 2
premise_z = 3
hypothesis_x = 7
hypothesis_y = 2
hypothesis_z = 3

# Check if the hypothesis values contradict the premise values
if hypothesis_x <= premise_x and hypothesis_y <= premise_y and hypothesis_z <= premise_z:
    # The hypothesis values do not contradict the premise values, so we can infer entailment
    label = "entailment"
else:
    # The hypothesis values contradict the premise values, so we can infer contradiction
    label = "contradiction"

print(label)
