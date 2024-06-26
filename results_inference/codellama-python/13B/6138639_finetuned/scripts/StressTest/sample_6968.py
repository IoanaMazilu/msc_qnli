property_size_premise = 900
property_size_hypothesis = 400
price_premise = 1500
price_hypothesis = 1500

# the hypothesis refers to the size of the property and the price mentioned in the premise
if property_size_hypothesis!= property_size_premise:
    # check if the size of the property in the hypothesis contradicts the size of the property in the premise
    label = "contradiction"
elif price_hypothesis!= price_premise:
    # check if the price in the hypothesis contradicts the price in the premise
    label = "contradiction"
else:
    # the premise gives the size of the property and the price, but does not mention the number of additions
    # any number of additions is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
