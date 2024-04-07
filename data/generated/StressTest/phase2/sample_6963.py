# Premise: In a locality, the prevailing price of a 700 square feet property last year was US Dollar 1000.
# Hypothesis: In a locality, the prevailing price of a less than 800 square feet property last year was US Dollar 1000.
# Golden Label: entailment

property_size_premise = 700
property_price_premise = 1000
property_size_hypothesis = 800
property_price_hypothesis = 1000

# the hypothesis refers to the price and size of a property mentioned in the premise
if property_price_premise != property_price_hypothesis:
    # check if the price of the property in the hypothesis contradicts the price of the property in the premise
    label = "contradiction"
elif property_size_hypothesis <= property_size_premise:
    # check if the size of the property in the hypothesis contradicts the size of the property in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

