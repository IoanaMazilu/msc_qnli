property_size_premise = 900
property_size_hypothesis = 800

# the hypothesis refers to the size of the property mentioned in the premise
if property_size_hypothesis <= property_size_premise:
    # check if the estimate of 'property_size_hypothesis' contradicts the size of the property in the premise
    label = "contradiction"
elif property_size_hypothesis > property_size_premise:
    # check if the hypothesis value is greater than the estimate of the property size in the premise
    label = "entailment"
else:
    # if the hypothesis value and estimate do not contradict the premise size, we can infer neutrality
    label = "neutral"

print(label)
