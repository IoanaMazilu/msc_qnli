# Define the variables for the premise
distance_1 = 240
speed_1 = 60
distance_2 = 120
speed_2 = 40

# Define the variables for the hypothesis
total_distance_hypothesis = 340

# The hypothesis refers to the total distance driven by Joe, which is also mentioned in the premise
if distance_1 + distance_2 > total_distance_hypothesis:
    # Check if the total distance driven by Joe contradicts the hypothesis
    label = "contradiction"
else:
    # If the total distance driven by Joe does not contradict the hypothesis, we can infer entailment
    label = "entailment"

print(label)
