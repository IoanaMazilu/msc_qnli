property_size_premise = 900
property_size_hypothesis = 800
price_premise = 1500
price_hypothesis = 1500

# the hypothesis refers to the size of the property and its price mentioned in the premise
if property_size_premise!= property_size_hypothesis:
    # check if the property size in the hypothesis contradicts the property size reported in the premise
    label = "contradiction"
elif price_hypothesis!= price_premise:
    # check if the price in the hypothesis contradicts the price reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
