# Define variables for the entities in the premise and hypothesis
premise_time = 20
hypothesis_time = 90

# Check if the hypothesis time is greater than the premise time
if hypothesis_time > premise_time:
    # The hypothesis time contradicts the premise time
    label = "contradiction"
elif hypothesis_time == premise_time:
    # The hypothesis time is consistent with the premise time, no entailment or contradiction
    label = "neutral"
else:
    # The hypothesis time is less than the premise time, entailment
    label = "entailment"

print(label)
