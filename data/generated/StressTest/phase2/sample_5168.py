# Premise: A train travels from Albany to Syracuse, a distance of 120 miles, at the average rate of 50 miles per hour.
# Hypothesis: A train travels from Albany to Syracuse, a distance of less than 120 miles, at the average rate of 50 miles per hour.
# Golden Label: contradiction

distance_premise = 120
distance_hypothesis = 120
average_speed_premise = 50
average_speed_hypothesis = 50

# the hypothesis refers to the distance and average speed of the train mentioned in the premise
if distance_hypothesis >= distance_premise:
    # check if the hypothesis estimate contradicts the distance reported in the premise
    label = "contradiction"
elif average_speed_hypothesis != average_speed_premise:
    # check if the average speed in the hypothesis contradicts the average speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

