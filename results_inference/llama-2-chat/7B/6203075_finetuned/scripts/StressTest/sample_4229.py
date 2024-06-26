speed_premise = 30
speed_hypothesis = 30

# the hypothesis refers to the speed at which Cara drives from City A to City B
if speed_hypothesis >= speed_premise:
    # check if the hypothesis speed contradicts the premise speed
    label = "contradiction"
else:
    # if the hypothesis speed is less than the premise speed, we can infer entailment
    label = "entailment"

print(label)
