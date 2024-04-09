jogging_speed_premise = 4
jogging_speed_hypothesis = float(input("Enter jogging speed (less than 4): "))
walking_speed_premise = 8

# the hypothesis refers to the jogging speed and walking speed mentioned in the premise
if jogging_speed_hypothesis < jogging_speed_premise:
    # check if the estimate of 'jogging_speed_hypothesis' contradicts the jogging speed in the premise
    label = "contradiction"
elif jogging_speed_hypothesis == jogging_speed_premise:
    # check if the jogging speed in the hypothesis is consistent with the premise
    label = "neutral"
else:
    # if the hypothesis value and estimate do not contradict the premise ones, we can infer entailment
    label = "entailment"

# check if the walking speed in the hypothesis is consistent with the premise
if walking_speed_premise == walking_speed_hypothesis:
    # check if the walking speed in the hypothesis is consistent with the premise
    label = "entailment"
else:
    # if the walking speed in the hypothesis contradicts the premise, we can infer contradiction
    label = "contradiction"

print(label)
