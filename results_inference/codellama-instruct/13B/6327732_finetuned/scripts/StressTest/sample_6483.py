distance_premise = 20
distance_hypothesis = 80
walking_speed_premise = 4
walking_speed_hypothesis = 4
running_speed_premise = 6
running_speed_hypothesis = 6

# the hypothesis refers to the distance between their homes, which is also mentioned in the premise
if distance_hypothesis <= distance_premise:
    # check if the hypothesis value contradicts the estimate of more than 'distance_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance between their homes
    # any distance greater than 'distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

# the hypothesis refers to the walking speed of Maxwell, which is also mentioned in the premise
if walking_speed_hypothesis!= walking_speed_premise:
    # check if the hypothesis value contradicts the walking speed in the premise
    label = "contradiction"

# the hypothesis refers to the running speed of Brad, which is also mentioned in the premise
if running_speed_hypothesis!= running_speed_premise:
    # check if the hypothesis value contradicts the running speed in the premise
    label = "contradiction"

print(label)