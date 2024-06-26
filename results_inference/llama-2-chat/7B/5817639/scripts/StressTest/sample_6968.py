property_size_premise = 900
property_size_hypothesis = 400

# the hypothesis talks about a different property size than the premise
if property_size_hypothesis <= property_size_premise:
    # check if the hypothesis value contradicts the estimate of the property size in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the property size
    # any property size greater than 'property_size_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
