# Premise: If the distance between their homes is 40 kilometers, Maxwell's walking speed is 4 km/h, and Brad's running speed is 6 km/h, what is the distance traveled by Brad?
# Hypothesis: If the distance between their homes is 70 kilometers, Maxwell's walking speed is 4 km/h, and Brad's running speed is 6 km/h, what is the distance traveled by Brad?
# Golden Label: contradiction

distance_premise = 40
distance_hypothesis = 70
maxwell_speed_premise = maxwell_speed_hypothesis = 4
brad_speed_premise = brad_speed_hypothesis = 6

# the hypothesis refers to the distance between homes, Maxwell's speed and Brad's speed
if distance_premise != distance_hypothesis:
    # check if the distance in the hypothesis contradicts the distance in the premise
    label = "contradiction"
elif maxwell_speed_premise != maxwell_speed_hypothesis or brad_speed_premise != brad_speed_hypothesis:
    # check if the speeds in the hypothesis contradict the speeds in the premise
    label = "contradiction"
else:
    # if none of the variables in the hypothesis contradict the premise, we infer neutrality
    # as the premise does not provide any information about the distance traveled by Brad
    label = "neutral"

print(label)

