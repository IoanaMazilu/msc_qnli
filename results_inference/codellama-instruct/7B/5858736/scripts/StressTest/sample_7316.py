stretch_time_premise = 30
stretch_time_hypothesis = 80

if stretch_time_hypothesis <= stretch_time_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
