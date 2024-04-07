# Premise: While planning their outing, Abhishek understood that their boat could travel with a speed of 12 kmph in still water.
# Hypothesis: While planning their outing, Abhishek understood that their boat could travel with a speed of less than 52 kmph in still water.
# Golden Label: entailment

boat_speed_premise = 12
boat_speed_hypothesis = 52

# the hypothesis refers to the boat speed which is also mentioned in the premise
if boat_speed_premise >= boat_speed_hypothesis:
    # check if the speed from the premise contradicts the hypothesis estimate of less than 'boat_speed_hypothesis'
    label = "contradiction"
else:
    # if the premise value does not contradict the hypothesis estimate, we can infer entailment
    label = "entailment"

print(label)

