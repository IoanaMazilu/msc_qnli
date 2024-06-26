bird_speed_premise_first = 4
bird_speed_hypothesis_first = 7

if bird_speed_hypothesis_first <= bird_speed_premise_first:
    label = "contradiction"
else:
    label = "neutral"

print(label)
