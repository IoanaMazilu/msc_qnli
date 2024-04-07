# Premise: Jake drives at a constant speed of more than 19 km per hour.
# Hypothesis: Jake drives at a constant speed of 29 km per hour.
# Golden Label: neutral

speed_premise = 19
speed_hypothesis = 29

# the hypothesis refers to the speed that Jake drives, which is also mentioned in the premise
if speed_hypothesis <= speed_premise:
    # check if the speed in the hypothesis contradicts the minimum speed mentioned in the premise
    label = "contradiction"
else:
    # the premise gives only a minimum speed
    # any speed greater than 'speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

