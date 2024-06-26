train_code_premise = 12
train_code_hypothesis = 62
panda_code_premise = 18
panda_code_hypothesis = 18

# the hypothesis refers to the codes for TRAIN and PANDA mentioned in the premise
if train_code_premise >= train_code_hypothesis:
    # check if the estimate of 'train_code_hypothesis' contradicts the code for TRAIN in the premise
    label = "contradiction"
elif panda_code_hypothesis != panda_code_premise:
    # check if the code for PANDA in the hypothesis contradicts the code for PANDA in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
