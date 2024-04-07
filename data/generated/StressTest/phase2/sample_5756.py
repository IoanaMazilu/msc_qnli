# Premise: When the river is running at 1 km/h, it takes the rower 1 hour to row to Big Rock and back.
# Hypothesis: When the river is running at 3 km/h, it takes the rower 1 hour to row to Big Rock and back.
# Golden Label: contradiction

river_speed_premise = 1
river_speed_hypothesis = 3
rowing_time_premise = 1
rowing_time_hypothesis = 1

# the hypothesis refers to the river speed and rowing time to Big Rock and back mentioned in the premise
if rowing_time_hypothesis != rowing_time_premise:
    # check if the rowing time in the hypothesis contradicts the rowing time reported in the premise
    label = "contradiction"
elif river_speed_hypothesis <= river_speed_premise:
    # check if the river speed in the hypothesis contradicts the river speed reported in the premise
    label = "contradiction"
else:
    # the premise gives only a specific river speed and rowing time
    # any higher river speed with the same rowing time is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

