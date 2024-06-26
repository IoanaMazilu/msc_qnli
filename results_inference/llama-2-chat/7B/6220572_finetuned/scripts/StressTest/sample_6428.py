sold_value_premise = 450
sold_value_hypothesis = 750

# the hypothesis refers to the value of the thing sold mentioned in the premise
if sold_value_hypothesis == sold_value_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # any value greater than'sold_value_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
