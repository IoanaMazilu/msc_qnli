speed_premise = 40
speed_hypothesis = 10

if speed_hypothesis <= speed_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
