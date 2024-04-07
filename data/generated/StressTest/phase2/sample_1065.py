# Premise: If the speed of Mohan’s Mercedes is 35 km/hr and the distance traveled by the Ferrari is 490 km, find the total time taken for Rohit to drive that distance.
# Hypothesis: If the speed of Mohan’s Mercedes is less than 65 km/hr and the distance traveled by the Ferrari is 490 km, find the total time taken for Rohit to drive that distance.
# Golden Label: entailment

mercedes_speed_premise = 35
mercedes_speed_hypothesis = 65
ferrari_distance_premise = 490
ferrari_distance_hypothesis = 490

# the hypothesis refers to the speed of Mohan's Mercedes and the distance traveled by the Ferrari mentioned in the premise
if mercedes_speed_hypothesis < mercedes_speed_premise or ferrari_distance_hypothesis != ferrari_distance_premise:
    # check if the speed of Mohan's Mercedes in the hypothesis contradicts the speed in the premise
    # or if the distance traveled by the Ferrari in the hypothesis contradicts the distance in the premise
    label = "contradiction"
elif mercedes_speed_hypothesis > mercedes_speed_premise and ferrari_distance_hypothesis == ferrari_distance_premise:
    # if the speed of Mohan's Mercedes in the hypothesis is more than the speed in the premise
    # but the distance traveled by the Ferrari in the hypothesis is the same as the distance in the premise, we can infer entailment
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

