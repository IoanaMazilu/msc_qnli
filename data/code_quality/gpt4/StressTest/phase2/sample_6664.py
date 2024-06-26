joint_chiefs_premise = 6
joint_chiefs_hypothesis = 7

# the hypothesis talks about the number of Joint Chiefs in a meeting, referenced also in the premise
if joint_chiefs_hypothesis <= joint_chiefs_premise:
    # check if the hypothesis value contradicts the estimate of more than 'joint_chiefs_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of Joint Chiefs
    # any number of Joint Chiefs greater than 'joint_chiefs_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
