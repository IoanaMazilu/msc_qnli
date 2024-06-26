distance_homes_premise = 80
distance_homes_hypothesis = 20
maxwell_speed_premise = 4
maxwell_speed_hypothesis = 4
brad_speed_premise = 6
brad_speed_hypothesis = 6

# the hypothesis refers to the distance between homes, Maxwell's walking speed and Brad's running speed mentioned in the premise
if distance_homes_hypothesis >= distance_homes_premise:
    # check if the distance between homes in the hypothesis contradicts the estimate of less than 'distance_homes_premise'
    label = "contradiction"
elif maxwell_speed_hypothesis!= maxwell_speed_premise or brad_speed_hypothesis!= brad_speed_premise:
    # check if Maxwell's walking speed or Brad's running speed in the hypothesis contradicts the values reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance between homes
    # any distance less than 'distance_homes_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
