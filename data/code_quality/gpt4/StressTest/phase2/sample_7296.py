river_speed_premise = 2
river_speed_hypothesis = 1
rower_time_premise = 1
rower_time_hypothesis = 1

# the hypothesis talks about the river speed and the rower time to row to Big Rock and back, referenced also in the premise
if river_speed_premise <= river_speed_hypothesis:
    # check if the river speed in the premise contradicts the estimate of more than 'river_speed_hypothesis'
    label = "contradiction"
elif rower_time_premise != rower_time_hypothesis:
    # check if the rower time in the hypothesis contradicts the rower time reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
