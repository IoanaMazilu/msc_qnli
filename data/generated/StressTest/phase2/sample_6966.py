# Premise: The owner made some additions and the 900 square feet property is now fetching a price of US Dollar 1500.
# Hypothesis: The owner made some additions and the more than 800 square feet property is now fetching a price of US Dollar 1500.
# Golden Label: entailment

property_size_premise = 900
property_size_hypothesis = 800
property_price_premise = 1500
property_price_hypothesis = 1500

# the hypothesis refers to the size and price of the property mentioned in the premise
if property_size_premise <= property_size_hypothesis:
    # check if the size of the property in the premise contradicts the size mentioned in the hypothesis
    label = "contradiction"
elif property_price_premise != property_price_hypothesis:
    # check if the price of the property in the premise contradicts the price mentioned in the hypothesis
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

