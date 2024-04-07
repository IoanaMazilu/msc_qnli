# Premise: A train travels from Albany to Syracuse, a distance of 120 miles, at the average rate of 40 miles per hour.
# Hypothesis: A train travels from Albany to Syracuse, a distance of 820 miles, at the average rate of 40 miles per hour.
# Golden Label: contradiction

distance_premise = 120
distance_hypothesis = 820
speed_premise = 40
speed_hypothesis = 40

# the hypothesis refers to the distance from Albany to Syracuse and the average speed of the train, both mentioned in the premise
if distance_premise != distance_hypothesis:
    # check if the distance in the hypothesis contradicts the distance reported in the premise
    label = "contradiction"
elif speed_hypothesis != speed_premise:
    # check if the speed in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

