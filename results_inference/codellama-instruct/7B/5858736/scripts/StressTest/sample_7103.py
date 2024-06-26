# Define variables for the numerical entities in both inputs
distance_driven_premise = 240
speed_premise = 60
distance_driven_hypothesis = 140
speed_hypothesis = 60

# Extract all quantities as valid numbers
distance_driven_premise = float(distance_driven_premise)
speed_premise = float(speed_premise)
distance_driven_hypothesis = float(distance_driven_hypothesis)
speed_hypothesis = float(speed_hypothesis)

# Calculate the total time for each drive
time_driven_premise = distance_driven_premise / speed_premise
time_driven_hypothesis = distance_driven_hypothesis / speed_hypothesis

# Compare the total time for each drive
if time_driven_premise <= time_driven_hypothesis:
    # The hypothesis can be fully and explicitly entailed from the premise
    label = "entailment"
else:
    # The hypothesis contradicts the premise
    label = "contradiction"

print(label)
