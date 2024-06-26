joint_chiefs_premise = 4
joint_chiefs_hypothesis = 5

if joint_chiefs_hypothesis <= joint_chiefs_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
