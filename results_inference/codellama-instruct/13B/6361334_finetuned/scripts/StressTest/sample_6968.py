premise_area = 900
hypothesis_area = 400
premise_price = 1500
hypothesis_price = 1500

# the hypothesis refers to the area of the property and the price mentioned in the premise
if hypothesis_area <= premise_area:
    # check if the hypothesis value contradicts the estimate of more than 'premise_area'
    label = "contradiction"
elif hypothesis_price!= premise_price:
    # check if the price in the hypothesis contradicts the price reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
