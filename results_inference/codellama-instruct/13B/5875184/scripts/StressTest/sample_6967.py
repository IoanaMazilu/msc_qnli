premise_sqft = 800
hypothesis_sqft = 900

# the hypothesis refers to the number of square feet mentioned in the premise
if hypothesis_sqft <= premise_sqft:
    # check if the estimate of 'hypothesis_sqft' contradicts the number of square feet in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of square feet
    # any number of square feet greater than 'premise_sqft' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
