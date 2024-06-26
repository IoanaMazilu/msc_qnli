#property_size_premise = 900
#property_size_hypothesis = 400
#property_price_premise = 1500
#property_price_hypothesis = 1500

# the hypothesis refers to the size of the property and its price mentioned in the premise
# if the price is the same but the size is different, then it's a contradiction
if property_price_premise == property_price_hypothesis and property_size_premise!= property_size_hypothesis:
    label = "contradiction"
# if the price is different than the premise, then it's a contradiction
elif property_price_premise!= property_price_hypothesis:
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
#