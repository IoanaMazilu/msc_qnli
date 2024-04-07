# Premise: A train travels from Albany to Syracuse, a distance of 100 miles, at the average rate of 50 miles per hour.
# Hypothesis: A train travels from Albany to Syracuse, a distance of 300 miles, at the average rate of 50 miles per hour.
# Golden Label: contradiction

distance_premise = 100
distance_hypothesis = 300
speed_premise = 50
speed_hypothesis = 50

# the hypothesis refers to the distance and speed of the train travel mentioned in the premise
if distance_hypothesis != distance_premise:
    # check if the distance in the hypothesis contradicts the distance reported in the premise
    label = "contradiction"
elif speed_hypothesis != speed_premise:
    # check if the speed in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

