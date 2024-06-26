chief_naval_operations_premise = "Chief of Naval Operations"
chief_national_guard_bureau_premise = "Chief of the National Guard Bureau"
joint_chiefs_staff_premise = 7
joint_chiefs_staff_hypothesis = 6

# the hypothesis talks about the number of Joint Chiefs of Staff, referenced also in the premise
if joint_chiefs_staff_hypothesis <= joint_chiefs_staff_premise:
    # check if the hypothesis value contradicts the estimate of more than 'joint_chiefs_staff_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of Joint Chiefs of Staff
    # any number of Joint Chiefs of Staff greater than 'joint_chiefs_staff_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
