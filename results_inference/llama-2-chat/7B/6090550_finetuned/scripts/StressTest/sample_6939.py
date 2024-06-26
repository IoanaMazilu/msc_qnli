somenumber = 61

# the hypothesis states that Jose gets on the elevator on a floor less than 61, which is also mentioned in the premise
if somenumber >= 61:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise value, we can infer entailment
    label = "entailment"

print(label)
