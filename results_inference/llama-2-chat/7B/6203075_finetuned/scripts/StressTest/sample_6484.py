distance_premise = 80
distance_hypothesis = 20
maxwell_speed_premise = 4
maxwell_speed_hypothesis = 4
brad_speed_premise = 6
brad_speed_hypothesis = 6

# the hypothesis talks about the distance between their homes, Maxwell's speed and Brad's speed, which are also mentioned in the premise
if distance_hypothesis >= distance_premise:
    # check if the hypothesis value contradicts the estimate of less than 'distance_premise'
    label = "contradiction"
elif maxwell_speed_hypothesis!= maxwell_speed_premise or brad_speed_hypothesis!= brad_speed_premise:
    # check if the speed of Maxwell or Brad in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the distance between their homes
    # any distance less than 'distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
