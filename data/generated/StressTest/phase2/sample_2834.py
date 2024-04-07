# Premise: If the distance between their homes is 80 kilometers, Maxwell's walking speed is 4 km/h, and Brad's running speed is 6 km/h, what is the distance traveled by Brad?
# Hypothesis: If the distance between their homes is less than 80 kilometers, Maxwell's walking speed is 4 km/h, and Brad's running speed is 6 km/h, what is the distance traveled by Brad?
# Golden Label: contradiction

distance_homes_premise = 80
distance_homes_hypothesis = 80
maxwell_speed_premise = 4
maxwell_speed_hypothesis = 4
brad_speed_premise = 6
brad_speed_hypothesis = 6

# the hypothesis talks about the distance between homes, Maxwell's speed and Brad's speed
if distance_homes_hypothesis >= distance_homes_premise:
    # check if the hypothesis contradicts the premise's distance between homes
    label = "contradiction"
elif maxwell_speed_hypothesis != maxwell_speed_premise or brad_speed_hypothesis != brad_speed_premise:
    # check if the speeds in the hypothesis contradict the speeds in the premise
    label = "contradiction"
else:
    # the premise gives a specific distance, while the hypothesis gives a maximum possible distance
    # the speeds are the same in the premise and the hypothesis
    # therefore, the hypothesis does not contradict the premise, but it cannot be explicitly entailed from it either
    label = "neutral"

print(label)

