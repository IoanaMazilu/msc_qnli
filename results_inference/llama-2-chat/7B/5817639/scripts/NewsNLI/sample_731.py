# Define variables for premise and hypothesis
premise_birdies = 0
hypothesis_birdies = 0

# Extract numbers from premise and hypothesis
premise_total = 6
hypothesis_total = 6

# Compare values in premise and hypothesis
if hypothesis_birdies!= premise_birdies:
    # If the number of birdies in the hypothesis contradicts the premise, label is contradiction
    label = "contradiction"
elif hypothesis_total!= premise_total:
    # If the total score in the hypothesis contradicts the premise, label is contradiction
    label = "contradiction"
else:
    # If the values in the hypothesis do not contradict the premise, label is entailment
    label = "entailment"

# Print label
print(label)
