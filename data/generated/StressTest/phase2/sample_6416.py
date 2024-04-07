# Premise: When the river is running at 2 km/h, it takes the rower 1 hour to row to Big Rock and back.
# Hypothesis: When the river is running at more than 2 km/h, it takes the rower 1 hour to row to Big Rock and back.
# Golden Label: contradiction

river_speed_premise = 2
river_speed_hypothesis = 2
rower_time_premise = 1
rower_time_hypothesis = 1

# the hypothesis refers to the river speed and the time it takes the rower to reach Big Rock, 
# both elements are also mentioned in the premise
if river_speed_hypothesis <= river_speed_premise:
    # the hypothesis suggests the river speed is more than 'river_speed_premise', 
    # if it isn't, it contradicts the premise
    label = "contradiction"
elif rower_time_hypothesis != rower_time_premise:
    # the hypothesis suggests the rower takes 1 hour to reach Big Rock, 
    # if it isn't the same as in the premise, it contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, 
    # it cannot be explicitly entailed from the premise due to the 'more than' condition in the hypothesis
    label = "neutral"

print(label)

