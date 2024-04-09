fraction_premise = 7/12
fraction_hypothesis = 7/12

# the hypothesis refers to the fraction of the sum of money T that Anup was asked to find, which is also mentioned in the premise
if fraction_hypothesis <= fraction_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # the premise gives an explicit fraction for the sum of money T that Anup was asked to find
    # any fraction greater than 'fraction_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
