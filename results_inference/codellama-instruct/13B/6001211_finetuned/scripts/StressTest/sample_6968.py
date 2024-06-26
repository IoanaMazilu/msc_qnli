property_size_premise = 900
property_size_hypothesis = 400
property_price_premise = 1500
property_price_hypothesis = 1500

# the hypothesis refers to the size and price of a property mentioned in the premise
if property_size_hypothesis!= property_size_premise:
    # check if the size of the property in the hypothesis contradicts the size of the property reported in the premise
    label = "contradiction"
elif property_price_hypothesis!= property_price_premise:
    # check if the price of the property in the hypothesis contradicts the price of the property reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
