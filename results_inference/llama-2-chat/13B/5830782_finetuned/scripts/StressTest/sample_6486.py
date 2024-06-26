rainfall_premise = 25
rainfall_hypothesis = 65

# the hypothesis refers to the total rainfall in Springdale during the first two weeks of March, which is also mentioned in the premise
if rainfall_premise >= rainfall_hypothesis:
    # check if the premise value contradicts the estimate of less than 'rainfall_hypothesis'
    label = "contradiction"
else:
    # the premise gives an exact value for the total rainfall
    # any value less than 'rainfall_hypothesis' is consistent with the hypothesis, but cannot be explicitly entailed from the hypothesis
    label = "entailment"

print(label)
