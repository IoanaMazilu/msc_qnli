imes_per_hour_jogging = 3
times_per_hour_walking = 6

jogging_speed_hypothesis = 7
walking_speed_hypothesis = 6

# the hypothesis refers to the jogging and walking speeds mentioned in the premise
if jogging_speed_hypothesis!= jogging_speed_premise:
    # check if the jogging speed in the hypothesis contradicts the jogging speed in the premise
    label = "contradiction"
elif walking_speed_hypothesis!= walking_speed_premise:
    # check if the walking speed in the hypothesis contradicts the walking speed in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
