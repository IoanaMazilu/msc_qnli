premise_samsung_percentage = 25
premise_iphone_percentage = 70
hypothesis_samsung_percentage = 75
hypothesis_iphone_percentage = 70

# the hypothesis refers to the percentage of users using Samsung and iPhone phones in the same company
if hypothesis_samsung_percentage <= premise_samsung_percentage:
    # check if the hypothesis value contradicts the estimate of more than 'premise_samsung_percentage'
    label = "contradiction"
elif hypothesis_iphone_percentage!= premise_iphone_percentage:
    # check if the hypothesis value contradicts the estimate of 'premise_iphone_percentage'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
