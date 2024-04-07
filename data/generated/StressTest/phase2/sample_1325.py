# Premise: If the distance between their homes is 70 kilometers, Maxwell's walking speed is 4 km/h, and Brad's running speed is 6 km/h, what is the distance traveled by Brad?
# Hypothesis: If the distance between their homes is 40 kilometers, Maxwell's walking speed is 4 km/h, and Brad's running speed is 6 km/h, what is the distance traveled by Brad?
# Golden Label: contradiction

distance_homes_premise = 70
distance_homes_hypothesis = 40
maxwell_speed_premise = 4
maxwell_speed_hypothesis = 4
brad_speed_premise = 6
brad_speed_hypothesis = 6

# The hypothesis refers to the same scenario as the premise, but with a different distance between the homes
if distance_homes_premise != distance_homes_hypothesis:
    # Check if the distance between the homes in the hypothesis contradicts the distance in the premise
    label = "contradiction"
elif maxwell_speed_premise != maxwell_speed_hypothesis or brad_speed_premise != brad_speed_hypothesis:
    # Check if the walking speed of Maxwell or the running speed of Brad in the hypothesis contradicts the speeds in the premise
    label = "contradiction"
else:
    # If the hypothesis values do not contradict the premise ones, then the relation is neutral as the hypothesis is not explicitly entailed from the premise
    label = "neutral"

print(label)

