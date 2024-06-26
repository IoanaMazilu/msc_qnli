floor_premise = 71
floor_hypothesis = 51
speed_premise = 93
speed_hypothesis = 93

# the hypothesis talks about the floor number and the elevator ride speed referenced also in the premise
if floor_hypothesis <= floor_premise:
    # check if the hypothesis value contradicts the estimate of more than 'floor_premise'
    label = "contradiction"
elif speed_hypothesis!= speed_premise:
    # check if the number of floors per minute in the hypothesis contradicts the number of floors per minute reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)
