boat_speed_premise = 52
boat_speed_hypothesis = 12

# the hypothesis talks about the speed of the boat in still water, also mentioned in the premise
if boat_speed_hypothesis >= boat_speed_premise:
    # check if the hypothesis value contradicts the estimate of less than 'boat_speed_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the speed of the boat
    # any speed less than 'boat_speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
