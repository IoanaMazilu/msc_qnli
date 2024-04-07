# Premise: A train travels from Albany to Syracuse, a distance of less than 300 miles, at the average rate of 50 miles per hour.
# Hypothesis: A train travels from Albany to Syracuse, a distance of 100 miles, at the average rate of 50 miles per hour.
# Golden Label: neutral

distance_premise = 300
distance_hypothesis = 100
speed_premise = 50
speed_hypothesis = 50

# the hypothesis refers to the distance between Albany to Syracuse and the average speed of the train, both mentioned in the premise
if distance_hypothesis >= distance_premise:
    # check if the distance in the hypothesis contradicts the estimate of less than 'distance_premise'
    label = "contradiction"
elif speed_hypothesis != speed_premise:
    # check if the speed in the hypothesis contradicts the speed mentioned in the premise
    label = "contradiction"
elif distance_hypothesis < distance_premise and speed_hypothesis == speed_premise:
    # the premise only gives an upper estimate for the distance, so any distance less than 'distance_premise' does not contradict the premise
    # however, because the exact distance is not stated in the premise, we cannot infer entailment
    label = "neutral"
else:
    label = "neutral"

print(label)

