# Premise: If the speed of Mohan’s Mercedes is less than 65 km/hr and the distance traveled by the Ferrari is 490 km, find the total time taken for Rohit to drive that distance.
# Hypothesis: If the speed of Mohan’s Mercedes is 35 km/hr and the distance traveled by the Ferrari is 490 km, find the total time taken for Rohit to drive that distance.
# Golden Label: neutral

speed_mercedes_premise = 65
speed_mercedes_hypothesis = 35
distance_ferrari_premise = 490
distance_ferrari_hypothesis = 490

# the hypothesis talks about the speed of Mohan's Mercedes and the distance traveled by Ferrari
# both these entities are also mentioned in the premise
if speed_mercedes_hypothesis >= speed_mercedes_premise:
    # check if the speed of Mohan's Mercedes in the hypothesis contradicts the premise
    label = "contradiction"
elif distance_ferrari_hypothesis != distance_ferrari_premise:
    # check if the distance traveled by Ferrari in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

