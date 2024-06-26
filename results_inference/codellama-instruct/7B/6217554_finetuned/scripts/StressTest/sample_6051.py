jog_speed_premise = 3
jog_speed_hypothesis = 4

if jog_speed_hypothesis <= jog_speed_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
