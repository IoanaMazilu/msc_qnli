# the hypothesis talks about the denominations of bonds sold, which is also referenced in the premise
if bonds_denominations_premise < 70:
    # the hypothesis states that the denominations are either $less than 70 or $100, which contradicts the premise
    label = "contradiction"
elif bonds_denominations_premise > 100:
    # the premise states that the denominations are either $50 or $100, which is not contradicted by the hypothesis
    label = "neutral"
else:
    # if the denominations in the premise are not less than 70 and not greater than 100, then the hypothesis cannot be entailed
    label = "neutral"

print(label)
