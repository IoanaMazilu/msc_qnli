# the hypothesis talks about the definition of a Sophie Germain prime, referenced also in the premise
if 8*p + 1!= p*p + 1:
    # check if the hypothesis estimate contradicts the premise definition
    label = "contradiction"
else:
    # the premise gives only a definition for the Sophie Germain prime
    # any definition consistent with the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
