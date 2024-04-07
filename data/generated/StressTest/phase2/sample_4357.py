# Premise: Assuming that Karen drives at an average speed of more than 20 mph and Tom drives at an average speed of 45 mph, how many H miles will Tom drive before Karen wins the bet?
# Hypothesis: Assuming that Karen drives at an average speed of 60 mph and Tom drives at an average speed of 45 mph, how many H miles will Tom drive before Karen wins the bet?
# Golden Label: neutral

karen_speed_premise = 20
tom_speed_premise = 45
karen_speed_hypothesis = 60
tom_speed_hypothesis = 45

# the hypothesis refers to the average speeds of Karen and Tom mentioned in the premise
if karen_speed_hypothesis <= karen_speed_premise:
    # check if the 'karen_speed_hypothesis' contradicts the number of karen speed in the premise
    label = "contradiction"
elif tom_speed_hypothesis != tom_speed_premise:
    # check if the 'tom_speed_hypothesis' contradicts the number of tom speed reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for Karen's speed
    # any speed of Karen greater than 'karen_speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

