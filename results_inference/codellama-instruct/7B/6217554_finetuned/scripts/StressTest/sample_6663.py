joint_chiefs_premise = 6
joint_chiefs_hypothesis = 6

# the hypothesis refers to the number of Joint Chiefs of Staff mentioned in the premise
if joint_chiefs_hypothesis >= joint_chiefs_premise:
    # check if the number of Joint Chiefs of Staff in the hypothesis contradicts the estimate of more than 'joint_chiefs_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of Joint Chiefs of Staff
    # any number of Joint Chiefs of Staff less than 'joint_chiefs_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
