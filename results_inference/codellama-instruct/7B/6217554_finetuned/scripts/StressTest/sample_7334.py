# the hypothesis refers to the percentage of Samsung phone users and the percentage of i phone users mentioned in the premise
if premise_samsung_phone_users_percentage_hypothesis >= premise_samsung_phone_users_percentage:
    # check if the percentage of Samsung phone users in the hypothesis contradicts the percentage of Samsung phone users reported in the premise
    label = "contradiction"
elif premise_iphone_phone_users_percentage_hypothesis!= premise_iphone_phone_users_percentage:
    # check if the percentage of i phone users in the hypothesis contradicts the percentage of i phone users reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
