# Premise: If the distance between their homes is more than 10 kilometers, Maxwell's walking speed is 4 km/h, and Brad's running speed is 6 km/h, what is the distance traveled by Brad?
# Hypothesis: If the distance between their homes is 80 kilometers, Maxwell's walking speed is 4 km/h, and Brad's running speed is 6 km/h, what is the distance traveled by Brad?
# Golden Label: neutral

distance_premise = 10
distance_hypothesis = 80

# the hypothesis refers to the distance between homes mentioned in the premise
if distance_hypothesis <= distance_premise:
    # check if the distance in the hypothesis contradicts the estimate of more than 'distance_premise' kilometers in the premise
    label = "contradiction"
else:
    # the premise gives only a lower bound for the distance
    # any distance greater than 'distance_premise' is consistent with the premise, but cannot be explicitly entailed from it
    label = "neutral"

print(label)

