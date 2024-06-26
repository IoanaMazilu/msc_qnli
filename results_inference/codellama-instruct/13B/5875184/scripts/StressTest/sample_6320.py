premise_apples = 4
hypothesis_apples = 6

# the hypothesis refers to the number of apples Maddie has after giving 2 to mike
if hypothesis_apples - 2 == premise_apples:
    # check if the hypothesis value contradicts the number of apples Maddie has in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of apples Maddie has
    # any number of apples greater than 'premise_apples' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
