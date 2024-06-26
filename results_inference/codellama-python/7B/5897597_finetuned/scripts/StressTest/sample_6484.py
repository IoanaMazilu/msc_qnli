distance_premise = 80
distance_hypothesis = 20
maxwell_speed_premise = 4
maxwell_speed_hypothesis = 4
brad_speed_premise = 6
brad_speed_hypothesis = 6

# the hypothesis refers to the distance between homes, Maxwell's walking speed and Brad's running speed mentioned in the premise
if distance_hypothesis >= distance_premise:
    # check if the distance in the hypothesis contradicts the estimate of less than 'distance_premise'
    label = "contradiction"
elif maxwell_speed_hypothesis!= maxwell_speed_premise:
    # check if Maxwell's walking speed in the hypothesis contradicts the speed mentioned in the premise
    label = "contradiction"
elif brad_speed_hypothesis!= brad_speed_premise:
    # check if Brad's running speed in the hypothesis contradicts the speed mentioned in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance between homes
    # any distance less than 'distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
