karen_speed_premise = 10
tom_speed_premise = 45
karen_speed_hypothesis = 60
tom_speed_hypothesis = 45

# the hypothesis refers to the driving speed of Karen and Tom mentioned in the premise
if karen_speed_hypothesis <= karen_speed_premise:
    # check if the speed of Karen in the hypothesis contradicts the speed of Karen in the premise
    label = "contradiction"
elif tom_speed_hypothesis != tom_speed_premise:
    # check if the speed of Tom in the hypothesis contradicts the speed of Tom in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the speed of Karen
    # any speed of Karen greater than 'karen_speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
