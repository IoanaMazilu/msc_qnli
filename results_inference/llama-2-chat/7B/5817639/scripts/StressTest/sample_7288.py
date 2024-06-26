joint_ownership_premise = 64000
joint_ownership_hypothesis = 14000

# the hypothesis refers to the amount of money in a business jointly owned by the speaker and two other persons
if joint_ownership_hypothesis <= joint_ownership_premise:
    # check if the hypothesis value contradicts the estimate of less than 'joint_ownership_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of money in the business
    # any amount of money greater than 'joint_ownership_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
