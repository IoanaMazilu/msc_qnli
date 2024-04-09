nice_gift_premise = 5
nice_gift_hypothesis = float(6) # assume the hypothesis value is a valid number

# check if the hypothesis value exceeds the premise value
if nice_gift_hypothesis > nice_gift_premise:
    # the hypothesis value contradicts the premise value
    label = "contradiction"
elif nice_gift_hypothesis == nice_gift_premise:
    # the hypothesis value is consistent with the premise value, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # the hypothesis value is greater than the premise value, and can be entailed from the premise
    label = "entailment"

print(label)
