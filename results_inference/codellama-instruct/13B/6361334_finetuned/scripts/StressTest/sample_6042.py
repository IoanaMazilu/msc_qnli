distance_premise = 40
distance_hypothesis = 10
walking_speed_premise = 4
running_speed_premise = 6

# the hypothesis refers to the distance between their homes, which is also mentioned in the premise
if distance_hypothesis <= distance_premise:
    # check if the hypothesis value contradicts the estimate of more than 'distance_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance between their homes
    # any distance greater than 'distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
