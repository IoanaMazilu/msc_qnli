distance_homes_premise = 20
distance_homes_hypothesis = 80
maxwell_speed_premise = 4
maxwell_speed_hypothesis = 4
brad_speed_premise = 6
brad_speed_hypothesis = 6

# the hypothesis refers to the same situation as the premise, but with a different distance between the homes

if distance_homes_hypothesis <= distance_homes_premise:
    # check if the hypothesis value contradicts the distance between homes in the premise
    label = "contradiction"
elif maxwell_speed_hypothesis != maxwell_speed_premise or brad_speed_hypothesis != brad_speed_premise:
    # check if the walking speed of Maxwell or the running speed of Brad in the hypothesis contradicts the values reported in the premise
    label = "contradiction"
else:
    # the premise gives a specific distance between the homes
    # any distance less than 'distance_homes_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
