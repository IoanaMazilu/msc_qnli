distance_premise = 80
distance_hypothesis = 20
maxwell_speed_premise = 4
maxwell_speed_hypothesis = 4
brad_speed_premise = 6
brad_speed_hypothesis = 6

# the hypothesis talks about the distance between their homes, referenced also in the premise
if distance_hypothesis >= distance_premise:
    # check if the hypothesis value contradicts the estimate of less than 'distance_premise'
    label = "contradiction"
elif maxwell_speed_hypothesis!= maxwell_speed_premise:
    # check if the walking speed in the hypothesis contradicts the walking speed reported in the premise
    label = "contradiction"
elif brad_speed_hypothesis!= brad_speed_premise:
    # check if the running speed in the hypothesis contradicts the running speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
