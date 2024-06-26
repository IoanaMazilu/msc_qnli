property_size_premise = 900
property_size_hypothesis = 400
price_premise = 1500
price_hypothesis = 1500

# the hypothesis refers to the size of the property and the price mentioned in the premise
if property_size_premise!= property_size_hypothesis:
    # check if the property size in the hypothesis contradicts the property size reported in the premise
    label = "contradiction"
elif price_premise!= price_hypothesis:
    # check if the price in the hypothesis contradicts the price reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
