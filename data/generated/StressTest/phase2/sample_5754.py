# Premise: When the river is running at 1 km/h, it takes the rower 1 hour to row to Big Rock and back.
# Hypothesis: When the river is running at less than 2 km/h, it takes the rower 1 hour to row to Big Rock and back.
# Golden Label: entailment

river_speed_premise = 1
river_speed_hypothesis = 2
row_time_premise = 1
row_time_hypothesis = 1

# the hypothesis talks about the river speed and the rower's time to Big Rock, both referenced also in the premise
if (row_time_hypothesis != row_time_premise) or (river_speed_hypothesis <= river_speed_premise):
    # check if the time in the hypothesis contradicts the time in the premise or if the speed in the hypothesis contradicts the speed in the premise
    label = "contradiction"
elif river_speed_hypothesis > river_speed_premise:
    # the premise gives a specific speed for the river
    # any speed greater than 'river_speed_premise' is consistent with the premise, but the hypothesis is talking about speeds less than 'river_speed_hypothesis'
    label = "neutral"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

