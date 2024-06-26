premise_rainfall = 25
hypothesis_rainfall = 25

# the hypothesis refers to the total rainfall in Springdale mentioned in the premise
if hypothesis_rainfall <= premise_rainfall:
    # check if the estimate of 'hypothesis_rainfall' contradicts the total rainfall in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the total rainfall
    # any total rainfall greater than 'premise_rainfall' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
