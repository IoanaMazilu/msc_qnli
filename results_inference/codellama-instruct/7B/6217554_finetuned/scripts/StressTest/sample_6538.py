speed_premise = 50
speed_hypothesis = 30

if speed_hypothesis >= speed_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
