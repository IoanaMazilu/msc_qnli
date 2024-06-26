samsung_users_premise = 25
samsung_users_hypothesis = 75
iphone_users_premise = 70
iphone_users_hypothesis = 70

# the hypothesis refers to the percentage of Samsung and iPhone users in the same company
if samsung_users_hypothesis <= samsung_users_premise:
    # check if the percentage of Samsung users in the hypothesis contradicts the estimate of more than'samsung_users_premise'
    label = "contradiction"
elif iphone_users_hypothesis!= iphone_users_premise:
    # check if the percentage of iPhone users in the hypothesis contradicts the percentage of iPhone users reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of Samsung users
    # any percentage of Samsung users greater than'samsung_users_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
