property_size_premise = 800
property_size_hypothesis = 900
price_premise = 1500
price_hypothesis = 1500

# the hypothesis talks about the size of the property and its price, referenced also in the premise
if price_hypothesis!= price_premise:
    # check if the price in the hypothesis contradicts the price reported in the premise
    label = "contradiction"
elif property_size_hypothesis <= property_size_premise:
    # check if the size of the property in the hypothesis contradicts the estimate of more than 'property_size_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the size of the property
    # any size of the property greater than 'property_size_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)