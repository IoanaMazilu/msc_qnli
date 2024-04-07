# Premise: The distance between their homes is more than 12 kilometers, Ella's walking speed is 5 km/h, and Ed's walking speed is 3 km/h.
# Hypothesis: The distance between their homes is 42 kilometers, Ella's walking speed is 5 km/h, and Ed's walking speed is 3 km/h.
# Golden Label: neutral

distance_premise = 12
distance_hypothesis = 42
speed_ella_premise = speed_ella_hypothesis = 5
speed_ed_premise = speed_ed_hypothesis = 3

# the hypothesis refers to the distance between the homes and the walking speeds of Ella and Ed, mentioned in the premise
if distance_hypothesis <= distance_premise:
    # check if the estimated distance in the hypothesis contradicts the estimate in the premise
    label = "contradiction"
elif speed_ella_hypothesis != speed_ella_premise or speed_ed_hypothesis != speed_ed_premise:
    # check if the walking speeds in the hypothesis contradict the ones reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance
    # any distance greater than 'distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

