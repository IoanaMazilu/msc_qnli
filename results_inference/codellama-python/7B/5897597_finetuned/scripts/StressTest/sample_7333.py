samsung_phone_premise = 25
samsung_phone_hypothesis = 75
iphone_premise = 70
iphone_hypothesis = 70
samsung_phone_company_premise = 85
samsung_phone_company_hypothesis = 85

# the hypothesis refers to the percentage of Samsung phone users, i phone users and the percentage of Samsung phone users in the company, all mentioned in the premise
if samsung_phone_hypothesis <= samsung_phone_premise:
    # check if the percentage of Samsung phone users in the hypothesis contradicts the estimate of more than'samsung_phone_premise'
    label = "contradiction"
elif iphone_hypothesis!= iphone_premise:
    # check if the percentage of i phone users in the hypothesis contradicts the percentage of i phone users reported in the premise
    label = "contradiction"
elif samsung_phone_company_hypothesis!= samsung_phone_company_premise:
    # check if the percentage of Samsung phone users in the company in the hypothesis contradicts the percentage of Samsung phone users in the company reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of Samsung phone users
    # any percentage of Samsung phone users greater than'samsung_phone_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)