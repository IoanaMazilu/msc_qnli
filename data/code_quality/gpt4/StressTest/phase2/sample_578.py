speed_premise = 40
speed_hypothesis = 40

# the hypothesis refers to Bob's driving speed from City A to City B, mentioned also in the premise
if speed_hypothesis >= speed_premise:
    # check if the 'speed_hypothesis' contradicts the speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis speed does not contradict the premise speed, we can infer entailment
    label = "entailment"

print(label)
