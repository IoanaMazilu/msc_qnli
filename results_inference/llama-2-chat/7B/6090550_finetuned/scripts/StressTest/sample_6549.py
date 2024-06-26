bird1_speed_premise = 4
bird1_speed_hypothesis = 7
bird2_speed_premise = 1
bird2_speed_hypothesis = 1

# the hypothesis refers to the speed of two birds flying towards each other, mentioned in the premise
if bird1_speed_premise > bird1_speed_hypothesis:
    label = "entailment"
elif bird1_speed_premise < bird1_speed_hypothesis:
    label = "contradiction"
elif bird2_speed_premise!= bird2_speed_hypothesis:
    label = "contradiction"
else:
    label = "neutral"

print(label)
