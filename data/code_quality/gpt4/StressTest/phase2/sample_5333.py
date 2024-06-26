river_speed_premise = 1
river_speed_hypothesis = 1
time_to_rock_premise = 1
time_to_rock_hypothesis = 1

# the hypothesis refers to the river speed and the time it takes for the rower to row to Big Rock and back, which are also mentioned in the premise
if river_speed_hypothesis >= river_speed_premise:
    # check if the hypothesis value contradicts the statement that the river speed is less than 'river_speed_premise'
    label = "contradiction"
elif time_to_rock_hypothesis != time_to_rock_premise:
    # check if the time to row to Big Rock and back in the hypothesis contradicts the time reported in the premise
    label = "contradiction"
else:
    # if the values in the hypothesis do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
