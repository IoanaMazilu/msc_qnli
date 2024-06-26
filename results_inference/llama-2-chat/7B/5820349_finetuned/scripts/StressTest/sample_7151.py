joint_chiefs_premise = 5
joint_chiefs_hypothesis = 1

# the hypothesis refers to the number of Joint Chiefs of Staff mentioned in the premise
if joint_chiefs_hypothesis!= joint_chiefs_premise:
    # check if the number of Joint Chiefs in the hypothesis contradicts the number of Joint Chiefs reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
