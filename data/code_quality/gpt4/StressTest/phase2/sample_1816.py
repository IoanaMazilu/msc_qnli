distance_homes_premise = 70
distance_homes_hypothesis = 80
maxwell_speed = 4
brad_speed = 6

# the hypothesis talks about the distance between homes and the walking/running speed, referenced also in the premise
if distance_homes_hypothesis <= distance_homes_premise:
    # check if the hypothesis value contradicts the estimate of more than 'distance_homes_premise'
    label = "contradiction"
elif maxwell_speed != 4 or brad_speed != 6:
    # check if the speed of Maxwell or Brad in the hypothesis contradicts the speed mentioned in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance between homes
    # any distance greater than 'distance_homes_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
