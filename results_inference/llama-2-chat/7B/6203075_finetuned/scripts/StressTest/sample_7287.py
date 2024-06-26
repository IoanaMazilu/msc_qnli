business_value_premise = 14000
business_value_hypothesis = 64000

# the hypothesis refers to the value of a business, which is also mentioned in the premise
if business_value_hypothesis <= business_value_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif business_value_hypothesis > business_value_premise:
    # if the hypothesis value is greater than the premise value, it can be inferred as entailment
    label = "entailment"
else:
    # if the hypothesis value is equal to the premise value, it is neutral
    label = "neutral"

print(label)
