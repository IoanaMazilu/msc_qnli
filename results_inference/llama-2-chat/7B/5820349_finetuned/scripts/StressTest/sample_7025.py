speed_premise = 30
speed_hypothesis = 10

# the hypothesis refers to the speed of Cara's driving from City A to City B mentioned in the premise
if speed_hypothesis!= speed_premise:
    # check if the speed in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis speed does not contradict the premise speed, we can infer entailment
    label = "entailment"

print(label)
