samsung_phone_premise = 25
samsung_phone_hypothesis = 75
i_phone_premise = 70
i_phone_hypothesis = 70
samsung_phone_company_premise = 85
samsung_phone_company_hypothesis = 85

# the hypothesis talks about the percentage of Samsung phone and i phone users, referenced also in the premise
if samsung_phone_hypothesis <= samsung_phone_premise:
    # check if the percentage of Samsung phone users in the hypothesis contradicts the estimate of more than'samsung_phone_premise'
    label = "contradiction"
elif i_phone_hypothesis!= i_phone_premise:
    # check if the percentage of i phone users in the hypothesis contradicts the percentage of i phone users reported in the premise
    label = "contradiction"
elif samsung_phone_company_hypothesis!= samsung_phone_company_premise:
    # check if the percentage of Samsung phone users in the same company in the hypothesis contradicts the percentage of Samsung phone users in the same company reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
