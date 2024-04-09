property_size_premise = 900
property_size_hypothesis = 400
price_premise = 1500
price_hypothesis = 1500

# the hypothesis refers to the size of the property and its price mentioned in the premise
if property_size_premise!= property_size_hypothesis:
    # check if the size of the property in the hypothesis contradicts the size of the property reported in the premise
    label = "contradiction"
elif price_premise!= price_hypothesis:
    # check if the price of the property in the hypothesis contradicts the price of the property reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
