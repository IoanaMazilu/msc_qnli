speed_premise = 50
speed_hypothesis = 30

# the hypothesis refers to the constant speed of Cara during the drive from City A to City B mentioned in the premise
if speed_hypothesis >= speed_premise:
    # check if the speed in the hypothesis contradicts the estimate of less than'speed_premise'
    label = "contradiction"
else:
    # if the hypothesis speed does not contradict the premise speed, we can infer entailment
    label = "entailment"

print(label)
