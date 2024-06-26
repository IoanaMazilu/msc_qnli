samsung_phone_premise = 75
samsung_phone_hypothesis = 75
iphone_premise = 70
iphone_hypothesis = 70
samsung_phone_users_premise = 85
samsung_phone_users_hypothesis = 85

# the hypothesis refers to the percentage of Samsung phone users, the percentage of i phone users and the percentage of Samsung phone users in the company, all mentioned in the premise
if samsung_phone_hypothesis >= samsung_phone_premise:
    # check if the hypothesis value contradicts the estimate of less than'samsung_phone_premise'
    label = "contradiction"
elif iphone_hypothesis!= iphone_premise:
    # check if the percentage of i phone users in the hypothesis contradicts the percentage of i phone users reported in the premise
    label = "contradiction"
elif samsung_phone_users_hypothesis!= samsung_phone_users_premise:
    # check if the percentage of Samsung phone users in the hypothesis contradicts the percentage of Samsung phone users reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
