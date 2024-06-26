premise_samsung_percentage = 75
premise_iphone_percentage = 70
hypothesis_samsung_percentage = 75
hypothesis_iphone_percentage = 70

# the hypothesis refers to the percentage of users using Samsung and iPhone phones in the same company
if hypothesis_samsung_percentage <= premise_samsung_percentage:
    # check if the hypothesis value contradicts the estimate of more than 'premise_samsung_percentage'
    label = "contradiction"
elif hypothesis_iphone_percentage!= premise_iphone_percentage:
    # check if the number of sold pies in the hypothesis contradicts the number of sold pies reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
