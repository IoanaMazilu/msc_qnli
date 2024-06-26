distance_homes_premise = 40
distance_homes_hypothesis = 10
maxwell_speed_premise = 4
maxwell_speed_hypothesis = 4
brad_speed_premise = 6
brad_speed_hypothesis = 6

# the hypothesis refers to the distance between their homes, Maxwell's walking speed, and Brad's running speed mentioned in the premise
if distance_homes_hypothesis <= distance_homes_premise:
    # check if the hypothesis value contradicts the estimate of more than 'distance_homes_premise' kilometers between their homes
    label = "contradiction"
elif maxwell_speed_hypothesis!= maxwell_speed_premise or brad_speed_hypothesis!= brad_speed_premise:
    # check if the speed of Maxwell or Brad in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)