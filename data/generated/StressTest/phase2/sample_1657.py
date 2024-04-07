# Premise: While planning their outing, Abhishek understood that their boat could travel with a speed of less than 22 kmph in still water.
# Hypothesis: While planning their outing, Abhishek understood that their boat could travel with a speed of 12 kmph in still water.
# Golden Label: neutral

boat_speed_premise = 22
boat_speed_hypothesis = 12

# the hypothesis refers to the speed of the boat in still water mentioned in the premise
if boat_speed_hypothesis >= boat_speed_premise:
    # check if the speed in 'boat_speed_hypothesis' contradicts the premise that the boat speed is less than 'boat_speed_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the speed of the boat
    # any speed less than 'boat_speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

