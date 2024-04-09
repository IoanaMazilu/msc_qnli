joint_ownership_premise = 14000
joint_ownership_hypothesis = 24000

# the hypothesis refers to the amount of money in the business, which is also mentioned in the premise
if joint_ownership_hypothesis <= joint_ownership_premise:
    # check if the estimate of 'joint_ownership_hypothesis' contradicts the amount of money in the business reported in the premise
    label = "contradiction"
elif joint_ownership_hypothesis > joint_ownership_premise:
    # check if the hypothesis value contradicts the estimate of 'joint_ownership_premise'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
