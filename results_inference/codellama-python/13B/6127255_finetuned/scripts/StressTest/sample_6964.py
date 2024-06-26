price_premise = 1000
price_hypothesis = 1000
size_premise = 800
size_hypothesis = 700

# the hypothesis refers to the price and size of a property mentioned in the premise
if price_hypothesis!= price_premise:
    # check if the price in the hypothesis contradicts the price reported in the premise
    label = "contradiction"
elif size_hypothesis >= size_premise:
    # check if the size of the property in the hypothesis contradicts the premise of 'less than size_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the size of the property
    # any size less than'size_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
