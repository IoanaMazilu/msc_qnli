distance_home_premise = 40
walking_speed_premise = 4
running_speed_premise = 6

# the hypothesis refers to the distance traveled by Brad, which is a function of the distance between their homes and their speeds
if distance_home_premise <= 10:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance between their homes
    # any distance greater than 'distance_home_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
