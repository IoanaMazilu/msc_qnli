premise_rainfall = 25
hypothesis_rainfall = 65

# the hypothesis refers to the total rainfall in Springdale during the first two weeks of March
if premise_rainfall >= hypothesis_rainfall:
    # check if the estimate of 'hypothesis_rainfall' contradicts the total rainfall in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the total rainfall in Springdale during the first two weeks of March
    # any number of rainfall less than 'hypothesis_rainfall' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
