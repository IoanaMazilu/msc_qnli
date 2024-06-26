property_size_premise = 800
property_size_hypothesis = 900
price_premise = 1500
price_hypothesis = 1500

# the hypothesis refers to the property size and price mentioned in the premise
if property_size_hypothesis <= property_size_premise:
    # check if the property size in the hypothesis contradicts the property size in the premise
    label = "contradiction"
elif price_hypothesis!= price_premise:
    # check if the property price in the hypothesis contradicts the property price in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
