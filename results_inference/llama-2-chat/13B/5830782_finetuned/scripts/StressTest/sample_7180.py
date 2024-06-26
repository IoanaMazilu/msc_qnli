train_speed_premise = 60
train_speed_hypothesis = 80

# the hypothesis refers to the speed of the train mentioned in the premise
if train_speed_hypothesis!= train_speed_premise:
    # check if the speed of the train in the hypothesis contradicts the speed of the train reported in the premise
    label = "contradiction"
else:
    # if the hypothesis speed does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
