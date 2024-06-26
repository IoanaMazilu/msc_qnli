premise_apples = 48
hypothesis_apples = 88

# the hypothesis refers to the number of apples Maddie has after giving 22 to mike
if hypothesis_apples - premise_apples == 22:
    # check if the hypothesis value contradicts the number of apples Maddie has in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the number of apples Maddie has after giving 22 to mike
    # any number of apples greater than 'premise_apples' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
