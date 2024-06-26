distance_premise = 20
distance_hypothesis = 80
maxwell_speed_premise = 4
maxwell_speed_hypothesis = 4
brad_speed_premise = 6
brad_speed_hypothesis = 6

# the hypothesis refers to the distance between homes, Maxwell's walking speed and Brad's running speed mentioned in the premise
if distance_premise > distance_hypothesis:
    # check if the distance in the premise contradicts the estimate of less than 'distance_hypothesis'
    label = "contradiction"
elif maxwell_speed_premise!= maxwell_speed_hypothesis or brad_speed_premise!= brad_speed_hypothesis:
    # check if the speeds in the hypothesis contradict the speeds reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
