samsung_users_premise = 0.75
samsung_users_hypothesis = 0.75
iphone_users_premise = 0.70
iphone_users_hypothesis = 0.70

# the hypothesis refers to the percentage of i phone users in the same company as in the premise
if samsung_users_hypothesis <= samsung_users_premise:
    # check if the hypothesis value contradicts the estimate of more than'samsung_users_premise'
    label = "contradiction"
elif iphone_users_hypothesis!= iphone_users_premise:
    # check if the percentage of i phone users in the hypothesis contradicts the percentage of i phone users reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of i phone users
    # any percentage of i phone users less than 'iphone_users_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
