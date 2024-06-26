distance_homes_premise = 60
distance_homes_hypothesis = 70
maxwell_speed_premise = 4
maxwell_speed_hypothesis = 4
brad_speed_premise = 6
brad_speed_hypothesis = 6

# the hypothesis refers to the same situation as the premise
# first, it talks about the distance between their homes
if distance_homes_hypothesis <= distance_homes_premise:
    # check if the estimate of 'distance_homes_hypothesis' contradicts the known distance in the premise
    label = "contradiction"
# next, it talks about Maxwell's walking speed
elif maxwell_speed_hypothesis != maxwell_speed_premise:
    # check if the hypothesis value contradicts the known speed of Maxwell in the premise
    label = "contradiction"
# finally, it talks about Brad's running speed
elif brad_speed_hypothesis != brad_speed_premise:
    # check if the hypothesis value contradicts the known speed of Brad in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
