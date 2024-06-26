# Define variables with representative names for the numerical entities in both inputs
steps_climbed_premise = 60
time_premise = 40
steps_climbed_hypothesis = 80

# Extract all quantities as valid numbers (integers or floats)
steps_climbed_premise = int(steps_climbed_premise)
time_premise = int(time_premise)
steps_climbed_hypothesis = int(steps_climbed_hypothesis)

# Use brief comments to explain what comparison you do between the defined variables
if steps_climbed_hypothesis > steps_climbed_premise:
    # Check if the estimate of'steps_climbed_hypothesis' contradicts the number of steps climbed in the premise
    label = "contradiction"
elif time_premise!= time_premise:
    # Check if the number of seconds in the hypothesis contradicts the number of seconds reported in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
