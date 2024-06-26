distance_between_homes_premise = 110
distance_between_homes_hypothesis = 610
maxwell_speed_premise = 4
maxwell_speed_hypothesis = 4
brad_speed_premise = 7
brad_speed_hypothesis = 7

# the hypothesis refers to the same distances and speeds as the premise
if distance_between_homes_premise >= distance_between_homes_hypothesis:
    # check if the estimate of 'distance_between_homes_hypothesis' contradicts the specific distance in the premise
    label = "contradiction"
elif maxwell_speed_premise != maxwell_speed_hypothesis or brad_speed_premise != brad_speed_hypothesis:
    # check if the hypothesis contradicts the speed values given in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
