premise_samsung_percentage = 75
premise_iphone_percentage = 70
hypothesis_samsung_percentage = 85

# the hypothesis refers to the percentage of users using Samsung phone in the same company
if hypothesis_samsung_percentage <= premise_samsung_percentage:
    # check if the hypothesis value contradicts the estimate of more than 'premise_samsung_percentage'
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of users using Samsung phone
    # any percentage greater than 'premise_samsung_percentage' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

# calculate the percentage of i phone users
iphone_percentage = premise_iphone_percentage / (premise_samsung_percentage + premise_iphone_percentage)

# check if the hypothesis value contradicts the calculated percentage of i phone users
if hypothesis_samsung_percentage <= iphone_percentage:
    # check if the hypothesis value contradicts the calculated percentage of i phone users
    label = "contradiction"
else:
    # the hypothesis value does not contradict the calculated percentage of i phone users
    label = "entailment"

print(label)
