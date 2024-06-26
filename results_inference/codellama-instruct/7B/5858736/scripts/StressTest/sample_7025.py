# Define variables for the premise and hypothesis
speed_premise = 30
speed_hypothesis = 10

# Check if the hypothesis speed is less than or equal to the premise speed
if speed_hypothesis <= speed_premise:
    # If the hypothesis speed is less than or equal to the premise speed, we can infer entailment
    label = "entailment"
else:
    # If the hypothesis speed is greater than the premise speed, we can infer contradiction
    label = "contradiction"

print(label)
