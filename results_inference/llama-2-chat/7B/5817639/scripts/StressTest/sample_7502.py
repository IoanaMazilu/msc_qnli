# Define variables for premise and hypothesis
run_speed_premise = 9
run_speed_hypothesis = 10

# Check if the hypothesis value contradicts the premise value
if run_speed_hypothesis > run_speed_premise:
    # The hypothesis value contradicts the premise value, label it as contradiction
    label = "contradiction"
elif run_speed_hypothesis == run_speed_premise:
    # If the hypothesis value is equal to the premise value, label it as neutral
    label = "neutral"
else:
    # If the hypothesis value is less than the premise value, label it as entailment
    label = "entailment"

print(label)
