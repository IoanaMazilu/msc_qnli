samsung_phone_users_premise = 75
samsung_phone_users_hypothesis = 85
iphone_users_premise = 70
iphone_users_hypothesis = 70

# the hypothesis refers to the percentage of Samsung phone users, which is also mentioned in the premise
if samsung_phone_users_hypothesis <= samsung_phone_users_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif iphone_users_hypothesis!= iphone_users_premise:
    # check if the percentage of iPhone users in the hypothesis contradicts the percentage of iPhone users in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
