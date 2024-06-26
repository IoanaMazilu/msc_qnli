property_size_premise = 800
property_size_hypothesis = 700
property_price_premise = 1000
property_price_hypothesis = 1000

# the hypothesis talks about the price and size of a property, referenced also in the premise
if property_price_hypothesis!= property_price_premise:
    # check if the price of the property in the hypothesis contradicts the price of the property in the premise
    label = "contradiction"
elif property_size_hypothesis >= property_size_premise:
    # check if the size of the property in the hypothesis contradicts the estimate of less than 'property_size_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the size of the property
    # any size of property less than 'property_size_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
