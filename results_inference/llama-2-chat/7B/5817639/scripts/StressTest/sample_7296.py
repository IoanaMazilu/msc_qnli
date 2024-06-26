river_speed_premise = 2
river_speed_hypothesis = 1

# the hypothesis talks about the speed of the river, which is also mentioned in the premise
if river_speed_hypothesis <= river_speed_premise:
    # check if the hypothesis value contradicts the estimate of 'river_speed_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the speed of the river
    # any speed greater than 'river_speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
