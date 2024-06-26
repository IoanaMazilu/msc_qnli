speed_premise = 30
speed_hypothesis = 30

# the hypothesis refers to the speed of Cara's drive from City A to City B, mentioned in the premise
if speed_hypothesis >= speed_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
