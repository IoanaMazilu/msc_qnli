samsung_phone_users_premise = 25
samsung_phone_users_hypothesis = 75
iphone_users_premise = 70
iphone_users_hypothesis = 70
samsung_phone_users_company_premise = 85
samsung_phone_users_company_hypothesis = 85

# the hypothesis refers to the percentage of users using Samsung and iPhone phones in ABC limited and the same company
if samsung_phone_users_hypothesis <= samsung_phone_users_premise:
    # check if the hypothesis value contradicts the estimate of more than'samsung_phone_users_premise'
    label = "contradiction"
elif iphone_users_hypothesis!= iphone_users_premise:
    # check if the percentage of iPhone users in the hypothesis contradicts the percentage of iPhone users reported in the premise
    label = "contradiction"
elif samsung_phone_users_company_hypothesis!= samsung_phone_users_company_premise:
    # check if the percentage of Samsung phone users in the company in the hypothesis contradicts the percentage of Samsung phone users in the company reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of Samsung phone users
    # any percentage of Samsung phone users greater than'samsung_phone_users_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
