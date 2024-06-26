# The hypothesis refers to the same property mentioned in the premise, but with a different size
if property_size_hypothesis == 900:
    # The hypothesis value contradicts the premise value
    label = "contradiction"
elif property_size_hypothesis >= 800:
    # The hypothesis value is consistent with the premise value
    label = "entailment"
else:
    # If the hypothesis value is less than 800, it is neutral
    label = "neutral"

print(label)
