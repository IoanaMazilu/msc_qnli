distance_premise = 40
distance_hypothesis = 80
maxwell_speed = 4
brad_speed = 6

# the hypothesis talks about the distance between homes and speeds of Maxwell and Brad, referenced also in the premise
if distance_hypothesis!= distance_premise:
    # check if the distance in the hypothesis contradicts the distance in the premise
    label = "contradiction"
else:
    # the premise gives the distance between homes and speeds of Maxwell and Brad
    # any distance and speeds equal to the ones in the premise are consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
