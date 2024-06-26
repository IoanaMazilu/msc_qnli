karen_speed_premise = 80
karen_speed_hypothesis = 60
tom_speed_premise = 45
tom_speed_hypothesis = 45

# the hypothesis refers to the driving speeds of Karen and Tom mentioned in the premise
if karen_speed_hypothesis >= karen_speed_premise:
    # check if the estimate of 'karen_speed_hypothesis' contradicts the number of karen speed in the premise
    label = "contradiction"
elif tom_speed_hypothesis!= tom_speed_premise:
    # check if the number of tom speed in the hypothesis contradicts the number of tom speed reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the karen speed
    # any karen speed less than 'karen_speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
