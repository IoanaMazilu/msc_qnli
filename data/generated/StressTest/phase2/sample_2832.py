# Premise: If the distance between their homes is 80 kilometers, Maxwell's walking speed is 4 km/h, and Brad's running speed is 6 km/h, what is the distance traveled by Brad?
# Hypothesis: If the distance between their homes is more than 10 kilometers, Maxwell's walking speed is 4 km/h, and Brad's running speed is 6 km/h, what is the distance traveled by Brad?
# Golden Label: entailment

distance_between_homes_premise = 80
distance_between_homes_hypothesis = 10
maxwell_speed_premise = 4
maxwell_speed_hypothesis = 4
brad_speed_premise = 6
brad_speed_hypothesis = 6

# the hypothesis refers to the distance between homes, Maxwell's walking speed and Brad's running speed mentioned in the premise
if maxwell_speed_hypothesis != maxwell_speed_premise:
    # check if Maxwell's walking speed in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
elif brad_speed_hypothesis != brad_speed_premise:
    # check if Brad's running speed in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
elif distance_between_homes_hypothesis > distance_between_homes_premise:
    # check if the distance between homes in the hypothesis contradicts the distance reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

