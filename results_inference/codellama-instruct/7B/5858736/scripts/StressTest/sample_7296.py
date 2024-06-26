river_speed_premise = 2
river_speed_hypothesis = 1

# the hypothesis refers to the river speed mentioned in the premise
if river_speed_hypothesis <= river_speed_premise:
    # check if the estimate of 'river_speed_hypothesis' contradicts the river speed in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the river speed
    # any speed greater than 'river_speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
