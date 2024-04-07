# Premise: If the distance between their homes is 20 kilometers, Maxwell's walking speed is 4 km/h, and Brad's running speed is 6 km/h, what is the distance traveled by Brad?
# Hypothesis: If the distance between their homes is more than 20 kilometers, Maxwell's walking speed is 4 km/h, and Brad's running speed is 6 km/h, what is the distance traveled by Brad?
# Golden Label: contradiction

distance_homes_premise = 20
distance_homes_hypothesis = 20

# the hypothesis refers to the distance between homes mentioned in the premise
if distance_homes_premise > distance_homes_hypothesis:
    # check if the estimate of 'distance_homes_hypothesis' contradicts the distance in the premise
    label = "contradiction"
else:
    # the premise gives the exact distance between the homes
    # any distance greater than 'distance_homes_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

