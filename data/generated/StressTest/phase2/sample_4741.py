# Premise: If the distance between their homes is less than 80 kilometers, Maxwell's walking speed is 3 km/h, and Brad's running speed is 6 km/h, what is the distance traveled by Brad?
# Hypothesis: If the distance between their homes is 50 kilometers, Maxwell's walking speed is 3 km/h, and Brad's running speed is 6 km/h, what is the distance traveled by Brad?
# Golden Label: neutral

distance_premise = 80
distance_hypothesis = 50
maxwell_speed = 3
brad_speed = 6

# the hypothesis refers to the distance between homes, Maxwell's walking speed and Brad's running speed mentioned in the premise
if distance_hypothesis > distance_premise:
    # check if the distance in the hypothesis contradicts the estimate of less than 'distance_premise' in the premise
    label = "contradiction"
elif maxwell_speed != 3 or brad_speed != 6:
    # check if the speeds in the hypothesis contradict the speeds mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

