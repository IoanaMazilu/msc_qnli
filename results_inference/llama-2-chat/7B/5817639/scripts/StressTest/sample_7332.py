% Labels = entailment, contradiction, neutral

premise_users_samsung = 75
premise_users_iphone = 70
hypothesis_users_samsung = 25
hypothesis_users_iphone = 70

# Check if the hypothesis value contradicts the estimate of 'premise_users_samsung'
if hypothesis_users_samsung <= premise_users_samsung:
    label = "contradiction"
elif hypothesis_users_iphone!= premise_users_iphone:
    # Check if the number of i phone users in the hypothesis contradicts the number of i phone users reported in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
