# Premise: If the distance between their homes is 40 kilometers, Maxwell's walking speed is 4 km/h, and Brad's running speed is 6 km/h, what is the distance traveled by Brad?
# Hypothesis: If the distance between their homes is 80 kilometers, Maxwell's walking speed is 4 km/h, and Brad's running speed is 6 km/h, what is the distance traveled by Brad?
# Golden Label: contradiction

distance_premise = 40
distance_hypothesis = 80
maxwell_speed_premise = 4
maxwell_speed_hypothesis = 4
brad_speed_premise = 6
brad_speed_hypothesis = 6

# the hypothesis and premise talk about the same things: distance between homes, Maxwell's walking speed, and Brad's running speed
if distance_premise != distance_hypothesis:
    # check if the distance in the hypothesis contradicts the distance in the premise
    label = "contradiction"
elif maxwell_speed_premise != maxwell_speed_hypothesis:
    # check if Maxwell's speed in the hypothesis contradicts Maxwell's speed in the premise
    label = "contradiction"
elif brad_speed_premise != brad_speed_hypothesis:
    # check if Brad's speed in the hypothesis contradicts Brad's speed in the premise
    label = "contradiction"
else:
    # if all values in the hypothesis do not contradict the ones in the premise, we have neutrality
    label = "neutral"

print(label)

