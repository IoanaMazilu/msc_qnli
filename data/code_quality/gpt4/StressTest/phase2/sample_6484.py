distance_homes_premise = 80
distance_homes_hypothesis = 20
maxwell_speed_premise = 4
maxwell_speed_hypothesis = 4
brad_speed_premise = 6
brad_speed_hypothesis = 6

# the hypothesis talks about the same situation as the premise, but with a different distance between homes
if distance_homes_hypothesis >= distance_homes_premise:
    # check if the hypothesis distance contradicts the premise distance
    label = "contradiction"
elif maxwell_speed_hypothesis != maxwell_speed_premise or brad_speed_hypothesis != brad_speed_premise:
    # check if the speeds of Maxwell or Brad in the hypothesis contradict their speeds in the premise
    label = "contradiction"
elif distance_homes_hypothesis < distance_homes_premise:
    # the premise gives only an estimate for the distance between homes
    # any distance less than 'distance_homes_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
