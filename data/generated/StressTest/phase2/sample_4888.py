# Premise: Tom drives from town W to town B, driving at a constant speed of more than 40 miles per hour.
# Hypothesis: Tom drives from town W to town B, driving at a constant speed of 60 miles per hour.
# Golden Label: neutral

speed_premise = 40
speed_hypothesis = 60

# the hypothesis refers to the speed of driving from town W to town B mentioned in the premise
if speed_hypothesis <= speed_premise:
    # check if the speed in the hypothesis contradicts the speed in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the speed
    # any speed greater than 'speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

