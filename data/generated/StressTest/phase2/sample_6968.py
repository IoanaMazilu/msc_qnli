# Premise: The owner made some additions and the 900 square feet property is now fetching a price of US Dollar 1500.
# Hypothesis: The owner made some additions and the 400 square feet property is now fetching a price of US Dollar 1500.
# Golden Label: contradiction

property_size_premise = 900
property_size_hypothesis = 400
property_price_premise = 1500
property_price_hypothesis = 1500

# the hypothesis refers to the size and price of a property mentioned in the premise
if property_price_premise != property_price_hypothesis:
    # check if the property price in the hypothesis contradicts the property price reported in the premise
    label = "contradiction"
elif property_size_premise != property_size_hypothesis:
    # check if the property size in the hypothesis contradicts the property size reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

