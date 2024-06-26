driving_speed_premise = 60
driving_speed_hypothesis = 70

# the hypothesis refers to the driving speed and the stopping town, both mentioned in the premise
if driving_speed_premise > driving_speed_hypothesis:
    # check if the premise's speed contradicts the hypothesis's speed estimation
    label = "contradiction"
elif driving_speed_premise < driving_speed_hypothesis:
    # the premise's speed is less than the hypothesis's speed estimation
    # therefore, the premise does not contradict the hypothesis but can't be explicitly entailed from the premise
    label = "neutral"
else:
    # if the driving speed and the stopping town in the hypothesis do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
