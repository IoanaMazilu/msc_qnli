premise_price = 1000
premise_sqft = 800
hypothesis_price = 1000
hypothesis_sqft = 700

# the hypothesis refers to the price of a property with a square footage less than the premise
if hypothesis_sqft >= premise_sqft:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif hypothesis_price!= premise_price:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
