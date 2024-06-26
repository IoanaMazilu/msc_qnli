river_speed_premise = 1
river_speed_hypothesis = 3
time_premise = 1
time_hypothesis = 1

# The hypothesis refers to the speed of the river and the time it takes the rower to row to Big Rock and back, both mentioned in the premise.
if river_speed_hypothesis < river_speed_premise:
    # Check if the estimate of 'river_speed_hypothesis' contradicts the river speed given in the premise.
    label = "contradiction"
elif time_hypothesis != time_premise:
    # Check if the time given in the hypothesis contradicts the time mentioned in the premise.
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, but they also do not fully entail the premise, we infer neutrality.
    label = "neutral"

print(label)
