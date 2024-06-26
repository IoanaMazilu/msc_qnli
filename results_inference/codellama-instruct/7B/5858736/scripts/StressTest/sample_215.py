# Define variables for the premise and hypothesis
avg_speed_premise = 36
avg_speed_hypothesis = 36

# Check if the hypothesis is entailed from the premise
if avg_speed_hypothesis <= avg_speed_premise:
    # The hypothesis is entailed from the premise
    label = "entailment"
else:
    # The hypothesis is not entailed from the premise
    label = "contradiction"

print(label)
