# Premise: When the river is running at 2 km/h, it takes the rower 1 hour to row to Big Rock and back.
# Hypothesis: When the river is running at 7 km/h, it takes the rower 1 hour to row to Big Rock and back.
# Golden Label: contradiction

river_speed_premise = 2
river_speed_hypothesis = 7
time_premise = 1
time_hypothesis = 1

# the hypothesis talks about the time it takes for the rower to row to Big Rock and back, given a certain river speed
if river_speed_hypothesis == river_speed_premise and time_hypothesis == time_premise:
    # check if the river speed and time in the hypothesis match the ones in the premise
    label = "entailment"
elif river_speed_hypothesis != river_speed_premise and time_hypothesis == time_premise:
    # check if the river speed in the hypothesis contradicts the one in the premise, while the time is the same
    label = "contradiction"
else:
    # if the river speed and time in the hypothesis do not contradict or match the ones in the premise, we can infer neutrality
    label = "neutral"

print(label)

