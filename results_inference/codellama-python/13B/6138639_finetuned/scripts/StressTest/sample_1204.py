speed_to_beach_premise = 40
speed_to_beach_hypothesis = 80
speed_to_home_premise = 70
speed_to_home_hypothesis = 70

# the hypothesis talks about the speed of Carl's trip to the beach and his return home, referenced also in the premise
if speed_to_beach_hypothesis <= speed_to_beach_premise:
    # check if the hypothesis value contradicts the estimate of more than'speed_to_beach_premise'
    label = "contradiction"
elif speed_to_home_hypothesis!= speed_to_home_premise:
    # check if the speed to home in the hypothesis contradicts the speed to home reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the speed to the beach
    # any speed to the beach greater than'speed_to_beach_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
