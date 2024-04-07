# Premise: Richard began driving from home on a trip averaging 30 miles per hour.
# Hypothesis: Richard began driving from home on a trip averaging 40 miles per hour.
# Golden Label: contradiction

average_speed_premise = 30
average_speed_hypothesis = 40

# the hypothesis refers to the average speed of Richard's trip, which is also mentioned in the premise
if average_speed_hypothesis != average_speed_premise:
    # check if the average speed in the hypothesis contradicts the average speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

