premise_number = 4
hypothesis_number = 8

# the hypothesis refers to the number of squares of positive integers
if hypothesis_number <= premise_number:
    # check if the hypothesis value contradicts the estimate of 'premise_number'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of squares
    # any number of squares greater than 'premise_number' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
