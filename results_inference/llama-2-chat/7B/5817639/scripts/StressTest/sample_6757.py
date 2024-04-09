p = 4
h = 8

# the hypothesis talks about the number of P that Tom goes after, referenced also in the premise
if h <= p:
    # check if the hypothesis value contradicts the estimate of more than 'p'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of P
    # any number of P greater than 'p' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
