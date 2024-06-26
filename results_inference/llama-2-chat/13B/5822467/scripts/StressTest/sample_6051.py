jogging_speed_premise = 3
jogging_speed_hypothesis = 4
walking_speed_premise = 6

# the hypothesis refers to the jogging speed and walking speed mentioned in the premise
if jogging_speed_hypothesis <= jogging_speed_premise and walking_speed_premise == 6:
    # check if the hypothesis value contradicts the estimate of the jogging speed in the premise
    # and the walking speed in the premise is consistent with the walking speed in the hypothesis
    label = "neutral"
elif jogging_speed_hypothesis < jogging_speed_premise:
    # check if the hypothesis value contradicts the estimate of the jogging speed in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
