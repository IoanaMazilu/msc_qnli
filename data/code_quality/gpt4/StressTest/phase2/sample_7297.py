river_speed_premise = 1
river_speed_hypothesis = 2
rowing_time_premise = 1
rowing_time_hypothesis = 1

# the hypothesis refers to the speed of the river and the rowing time to Big Rock, also mentioned in the premise
if river_speed_hypothesis <= river_speed_premise:
    # check if the given river speed in the hypothesis contradicts the premise's minimum river speed
    label = "contradiction"
elif rowing_time_hypothesis != rowing_time_premise:
    # check if the rowing time in the hypothesis contradicts the rowing time in the premise
    label = "contradiction"
else:
    # the premise gives only a minimum speed for the river
    # any river speed greater than 'river_speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
