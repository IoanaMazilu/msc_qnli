property_size_premise = 900
property_size_hypothesis = 400
price_premise = 1500

# the hypothesis refers to the property size and price mentioned in the premise
if property_size_premise > property_size_hypothesis:
    # check if the estimate of 'property_size_hypothesis' contradicts the property size in the premise
    label = "contradiction"
elif property_size_hypothesis!= price_premise:
    # check if the price mentioned in the hypothesis contradicts the price reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)