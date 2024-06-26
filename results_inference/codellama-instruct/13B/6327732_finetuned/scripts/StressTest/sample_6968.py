premise_sqft = 900
hypothesis_sqft = 400
premise_price = 1500
hypothesis_price = 1500

# the hypothesis refers to the number of square feet and price mentioned in the premise
if hypothesis_sqft <= premise_sqft:
    # check if the estimate of 'hypothesis_sqft' contradicts the number of square feet in the premise
    label = "contradiction"
elif hypothesis_price!= premise_price:
    # check if the price in the hypothesis contradicts the price reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
