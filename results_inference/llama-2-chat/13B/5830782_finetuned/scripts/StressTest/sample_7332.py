samsung_users_premise = 75
samsung_users_hypothesis = 25
iphone_users_premise = 70
iphone_users_hypothesis = 70
samsung_users_company_premise = 85
samsung_users_company_hypothesis = 85

# the hypothesis refers to the percentage of Samsung and iPhone users in the company, as mentioned in the premise
if samsung_users_hypothesis > samsung_users_premise:
    # check if the estimate of'samsung_users_hypothesis' contradicts the number of Samsung users in the premise
    label = "contradiction"
elif iphone_users_hypothesis!= iphone_users_premise:
    # check if the percentage of iPhone users in the hypothesis contradicts the percentage of iPhone users reported in the premise
    label = "contradiction"
elif samsung_users_company_hypothesis!= samsung_users_company_premise:
    # check if the percentage of Samsung users in the company in the hypothesis contradicts the percentage of Samsung users in the company reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
