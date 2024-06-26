samsung_premise = 75
samsung_hypothesis = 75
iphone_premise = 70
iphone_hypothesis = 70

# the hypothesis refers to the percentage of Samsung and iPhone users mentioned in the premise
if samsung_hypothesis > samsung_premise:
    # check if the hypothesis value contradicts the percentage of Samsung users in the premise
    label = "contradiction"
elif iphone_hypothesis != iphone_premise:
    # check if the percentage of iPhone users in the hypothesis contradicts the percentage of iPhone users mentioned in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of users
    # any percentage less than or equal to the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
