# Premise: While planning their outing, Abhishek understood that their boat could travel with a speed of 12 kmph in still water.
# Hypothesis: While planning their outing, Abhishek understood that their boat could travel with a speed of 42 kmph in still water.
# Golden Label: contradiction

boat_speed_premise = 12
boat_speed_hypothesis = 42

# the hypothesis refers to the speed of the boat mentioned in the premise
if boat_speed_hypothesis != boat_speed_premise:
    # check if the speed of the boat in the hypothesis contradicts the speed of the boat reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
