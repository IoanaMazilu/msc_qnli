premise_sqft = 700
premise_price = 1000
hypothesis_sqft = 700
hypothesis_price = 1000

# the hypothesis refers to the price of a property with less than 700 square feet
# the premise mentions the price of a property with 700 square feet
if hypothesis_sqft >= premise_sqft:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif hypothesis_price!= premise_price:
    # check if the hypothesis price contradicts the premise price
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
