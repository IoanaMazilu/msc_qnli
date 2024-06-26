samsung_phone_users_premise = 75
samsung_phone_users_hypothesis = 25
iphone_users_premise = 70
iphone_users_hypothesis = 70

# the hypothesis refers to the percentage of Samsung and i phone users in the premise
if samsung_phone_users_hypothesis >= samsung_phone_users_premise:
    # check if the estimate of'samsung_phone_users_hypothesis' contradicts the number of Samsung phone users in the premise
    label = "contradiction"
elif iphone_users_hypothesis!= iphone_users_premise:
    # check if the number of i phone users in the hypothesis contradicts the number of i phone users reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
