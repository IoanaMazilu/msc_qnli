# Premise: If the distance between their homes is more than 20 kilometers, Maxwell's walking speed is 4 km/h, and Brad's running speed is 6 km/h, what is the distance traveled by Brad?
# Hypothesis: If the distance between their homes is 30 kilometers, Maxwell's walking speed is 4 km/h, and Brad's running speed is 6 km/h, what is the distance traveled by Brad?
# Golden Label: neutral

distance_premise = 20
distance_hypothesis = 30
maxwell_speed = 4
brad_speed = 6

# The hypothesis refers to the same situation as the premise but with a different distance
if distance_hypothesis <= distance_premise:
    # Check if the hypothesis distance contradicts the premise (more than 20km)
    label = "contradiction"
else:
    # The premise only provides an estimate for the distance (more than 20km)
    # Any distance greater than 'distance_premise' is consistent with the premise, but cannot be explicitly entailed from it
    label = "neutral"

print(label)
