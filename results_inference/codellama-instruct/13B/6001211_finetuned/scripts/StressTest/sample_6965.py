property_size_premise = 700
property_price_premise = 1000
property_size_hypothesis = 700
property_price_hypothesis = 1000

# the hypothesis refers to the price and size of a property mentioned in the premise
if property_size_hypothesis >= property_size_premise:
    # check if the size of the property in the hypothesis contradicts the size of the property in the premise
    label = "contradiction"
elif property_price_hypothesis!= property_price_premise:
    # check if the price of the property in the hypothesis contradicts the price of the property in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
