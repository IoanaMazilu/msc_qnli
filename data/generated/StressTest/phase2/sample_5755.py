# Premise: When the river is running at less than 2 km/h, it takes the rower 1 hour to row to Big Rock and back.
# Hypothesis: When the river is running at 1 km/h, it takes the rower 1 hour to row to Big Rock and back.
# Golden Label: neutral

river_speed_premise = 2
river_speed_hypothesis = 1
time_premise = 1
time_hypothesis = 1

# the hypothesis refers to the river speed and the time it takes the rower to do a round trip to Big Rock, as mentioned in the premise
if river_speed_hypothesis >= river_speed_premise:
    # check if the 'river_speed_hypothesis' contradicts the premise's claim of the river speed being less than 'river_speed_premise'
    label = "contradiction"
elif time_hypothesis != time_premise:
    # check if the time it takes the rower to do a round trip to Big Rock in the hypothesis contradicts that in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

