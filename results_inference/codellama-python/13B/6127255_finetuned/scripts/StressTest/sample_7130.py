fraction_premise = 7/12
fraction_hypothesis = 7/12

# the hypothesis refers to the fraction of the sum of money Anup was asked to find, which is also mentioned in the premise
if fraction_hypothesis <= fraction_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the premise gives the exact fraction of the sum of money Anup was asked to find
    # any fraction greater than 'fraction_premise' cannot be explicitly entailed from the premise, hence it's neutral
    label = "neutral"

print(label)
