property_size_premise = 800
property_size_hypothesis = 700

# the hypothesis refers to the size of the property mentioned in the premise
if property_size_hypothesis >= property_size_premise:
    # check if the hypothesis value contradicts the estimate of less than 'property_size_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the size of the property
    # any size less than 'property_size_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
