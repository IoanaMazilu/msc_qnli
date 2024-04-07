# Premise: If the distance between their homes is 50 kilometers, Maxwell's walking speed is 4 km/h, and Brad's running speed is 6 km/h, what is the distance traveled by Brad?
# Hypothesis: If the distance between their homes is more than 50 kilometers, Maxwell's walking speed is 4 km/h, and Brad's running speed is 6 km/h, what is the distance traveled by Brad?
# Golden Label: contradiction

distance_homes_premise = 50
distance_homes_hypothesis = 50
maxwell_speed_premise = 4
maxwell_speed_hypothesis = 4
brad_speed_premise = 6
brad_speed_hypothesis = 6

# the hypothesis refers to the distance between homes, Maxwell's walking speed and Brad's running speed mentioned in the premise
if distance_homes_hypothesis <= distance_homes_premise:
    # check if the estimate of 'distance_homes_hypothesis' contradicts the distance between homes in the premise
    label = "contradiction"
elif maxwell_speed_hypothesis != maxwell_speed_premise or brad_speed_hypothesis != brad_speed_premise:
    # check if the speeds of Maxwell and Brad in the hypothesis contradict the speeds reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance between homes
    # any distance greater than 'distance_homes_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

