property_size_premise = 700
property_size_hypothesis = 700

# the hypothesis talks about the size of a property in a locality, referenced also in the premise
if property_size_hypothesis >= property_size_premise:
    # check if the hypothesis value contradicts the estimate of less than 'property_size_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the size of a property
    # any size of property less than 'property_size_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
