# Premise: While planning their outing, Abhishek understood that their boat could travel with a speed of 12 kmph in still water.
# Hypothesis: While planning their outing, Abhishek understood that their boat could travel with a speed of less than 12 kmph in still water.
# Golden Label: contradiction

boat_speed_premise = 12
boat_speed_hypothesis = 12

# the hypothesis refers to the boat speed mentioned in the premise
if boat_speed_hypothesis >= boat_speed_premise:
    # check if the hypothesis value contradicts the boat speed in the premise
    label = "contradiction"
else:
    # if the boat speed in the hypothesis is less than the premise, then it is consistent with the premise but cannot be explicitly entailed from it
    label = "neutral"

print(label)
