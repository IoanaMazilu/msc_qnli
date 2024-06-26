samsung_phone_users_premise = 75
samsung_phone_users_hypothesis = 75
iphone_users_premise = 70
iphone_users_hypothesis = 70
samsung_phone_users_company_premise = 85
samsung_phone_users_company_hypothesis = 85

# the hypothesis refers to the percentage of users using Samsung and iPhone phones in ABC limited and in the same company
if samsung_phone_users_hypothesis >= samsung_phone_users_premise:
    # check if the percentage of Samsung phone users in the hypothesis contradicts the percentage of Samsung phone users in the premise
    label = "contradiction"
elif iphone_users_hypothesis!= iphone_users_premise:
    # check if the percentage of iPhone users in the hypothesis contradicts the percentage of iPhone users in the premise
    label = "contradiction"
elif samsung_phone_users_company_hypothesis!= samsung_phone_users_company_premise:
    # check if the percentage of Samsung phone users in the same company in the hypothesis contradicts the percentage of Samsung phone users in the same company in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
