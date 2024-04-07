# Premise: The owner made some additions and the more than 800 square feet property is now fetching a price of US Dollar 1500.
# Hypothesis: The owner made some additions and the 900 square feet property is now fetching a price of US Dollar 1500.
# Golden Label: neutral

property_size_premise = 800
property_size_hypothesis = 900
property_price_premise = 1500
property_price_hypothesis = 1500

# the hypothesis talks about the property size and price, referenced also in the premise
if property_size_hypothesis <= property_size_premise:
    # check if the hypothesis value contradicts the estimate of more than 'property_size_premise'
    label = "contradiction"
elif property_price_hypothesis != property_price_premise:
    # check if the property price in the hypothesis contradicts the property price reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the property size
    # any property size greater than 'property_size_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

