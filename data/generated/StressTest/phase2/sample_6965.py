# Premise: In a locality, the prevailing price of a 700 square feet property last year was US Dollar 1000.
# Hypothesis: In a locality, the prevailing price of a less than 700 square feet property last year was US Dollar 1000.
# Golden Label: contradiction

property_size_premise = 700
property_price_premise = 1000
property_size_hypothesis = 700
property_price_hypothesis = 1000

# the hypothesis talks about the price of a property with a size less than 'property_size_hypothesis', referenced also in the premise
if property_price_hypothesis != property_price_premise:
    # check if the price of the property in the hypothesis contradicts the price of the property in the premise
    label = "contradiction"
elif property_size_hypothesis == property_size_premise:
    # check if the size of the property in the hypothesis contradicts the size of the property in the premise
    label = "contradiction"
else:
    # the premise gives the price for a property of a specific size 
    # the hypothesis suggests a property of smaller size at the same price, which is not contradicting the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

