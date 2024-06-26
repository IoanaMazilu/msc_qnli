premise = "If the average speed of the whole journey was 36 mph, then what is Tom's speed driving from B to C in miles per hour?"
hypothesis = "If the average speed of the whole journey was less than 36 mph, then what is Tom's speed driving from B to C in miles per hour?"

# extract the numerical entities from the premise and hypothesis
premise_speed = 36
hypothesis_speed = 36

# compare the numerical entities
if premise_speed > hypothesis_speed:
    # the hypothesis value contradicts the premise value
    label = "contradiction"
elif premise_speed == hypothesis_speed:
    # the hypothesis value is consistent with the premise value
    label = "entailment"
else:
    # the hypothesis value is not explicitly entailed from the premise value
    label = "neutral"

print(label)
