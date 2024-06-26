samsung_phone_users_premise = 75
samsung_phone_users_hypothesis = 75
i_phone_users_premise = 70
i_phone_users_hypothesis = 70
samsung_phone_users_in_company_premise = 85
samsung_phone_users_in_company_hypothesis = 85

# the hypothesis refers to the percentage of Samsung phone users and i phone users mentioned in the premise
if samsung_phone_users_hypothesis >= samsung_phone_users_premise:
    # check if the estimate of'samsung_phone_users_hypothesis' contradicts the percentage of Samsung phone users in the premise
    label = "contradiction"
elif i_phone_users_hypothesis!= i_phone_users_premise:
    # check if the percentage of i phone users in the hypothesis contradicts the percentage of i phone users reported in the premise
    label = "contradiction"
elif samsung_phone_users_in_company_hypothesis!= samsung_phone_users_in_company_premise:
    # check if the percentage of Samsung phone users in the same company in the hypothesis contradicts the percentage of Samsung phone users in the same company reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
