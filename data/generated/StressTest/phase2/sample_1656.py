# Premise: While planning their outing, Abhishek understood that their boat could travel with a speed of 12 kmph in still water.
# Hypothesis: While planning their outing, Abhishek understood that their boat could travel with a speed of less than 22 kmph in still water.
# Golden Label: entailment

boat_speed_premise = 12
boat_speed_hypothesis = 22

# the hypothesis talks about the speed of the boat in still water, referenced also in the premise
if boat_speed_hypothesis < boat_speed_premise:
    # check if the hypothesis value contradicts the exact speed of 'boat_speed_premise' mentioned in the premise
    label = "contradiction"
elif boat_speed_hypothesis == boat_speed_premise:
    # check if the hypothesis value matches the exact speed of 'boat_speed_premise' mentioned in the premise
    label = "entailment"
else:
    # the premise gives an exact value for the speed of the boat
    # any speed less than 'boat_speed_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

