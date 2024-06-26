karen_speed_premise = 20
karen_speed_hypothesis = 60
tom_speed_premise = 45
tom_speed_hypothesis = 45

# the hypothesis refers to the average speed of both drivers
if karen_speed_hypothesis > karen_speed_premise and tom_speed_hypothesis > tom_speed_premise:
    # check if the estimate of 'karen_speed_hypothesis' and 'tom_speed_hypothesis' contradict the premise values
    label = "contradiction"
elif karen_speed_hypothesis == karen_speed_premise and tom_speed_hypothesis == tom_speed_premise:
    # check if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "neutral"

print(label)
