p_value = 8
h_value = 6

# check if the hypothesis value contradicts the estimate of 'p_value'
if h_value < p_value:
    label = "contradiction"
elif h_value > p_value:
    # the hypothesis value is consistent with the estimate of 'p_value', but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # the hypothesis value is equal to the estimate of 'p_value', so we can infer entailment
    label = "entailment"

print(label)
