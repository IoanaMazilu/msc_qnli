karen_speed_premise = 20
karen_speed_hypothesis = 60
tom_speed_premise = 45
tom_speed_hypothesis = 45

# the hypothesis refers to the driving speeds of Karen and Tom mentioned in the premise
if karen_speed_hypothesis <= karen_speed_premise:
    # check if the estimate of 'karen_speed_hypothesis' contradicts the number of karen's speed in the premise
    label = "contradiction"
elif tom_speed_hypothesis!= tom_speed_premise:
    # check if the number of tom's speed in the hypothesis contradicts the number of tom's speed reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for Karen's speed
    # any speed of Karen greater than 'karen_speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
