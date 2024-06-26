#property_size_premise = 700
#property_size_hypothesis = 700
#price_premise = 1000
#price_hypothesis = 1000

# the hypothesis refers to the size of a property and its price, both mentioned in the premise
# if the size of the property in the hypothesis is greater than or equal to the size of the property in the premise, then the price cannot be the same
if property_size_hypothesis >= property_size_premise:
    label = "contradiction"
# if the size of the property in the hypothesis is less than the size of the property in the premise, then the price could be the same
elif price_hypothesis == price_premise:
    label = "entailment"
else:
    label = "neutral"

print(label)
#