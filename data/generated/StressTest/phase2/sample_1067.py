# Premise: If the speed of Mohan’s Mercedes is 35 km/hr and the distance traveled by the Ferrari is 490 km, find the total time taken for Rohit to drive that distance.
# Hypothesis: If the speed of Mohan’s Mercedes is less than 35 km/hr and the distance traveled by the Ferrari is 490 km, find the total time taken for Rohit to drive that distance.
# Golden Label: contradiction

mercedes_speed_premise = 35
mercedes_speed_hypothesis = 35
ferrari_distance_premise = 490
ferrari_distance_hypothesis = 490

# the hypothesis refers to the speed of the Mercedes and the distance traveled by the Ferrari mentioned in the premise
if mercedes_speed_hypothesis >= mercedes_speed_premise:
    # check if the estimate of 'mercedes_speed_hypothesis' contradicts the speed of the Mercedes in the premise
    label = "contradiction"
elif ferrari_distance_hypothesis != ferrari_distance_premise:
    # check if the distance traveled by the Ferrari in the hypothesis contradicts the distance reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

