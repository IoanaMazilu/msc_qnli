p_value = 2
h_value = 8

# the hypothesis refers to the number of people Ana goes before, referenced in the premise
if h_value <= p_value:
    # check if the hypothesis value contradicts the estimate of more than 'p_value'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of people Ana goes before
    # any number of people greater than 'p_value' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
