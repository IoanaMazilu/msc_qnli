value_premise = 7/12
value_hypothesis = 7/12

# the hypothesis refers to the fraction of the sum of money Anup was asked to find, mentioned in the premise
if value_hypothesis <= value_premise:
    # check if the hypothesis value contradicts the fraction in the premise
    label = "contradiction"
else:
    # the premise gives the exact fraction of the sum of money Anup was asked to find
    # any fraction greater than 'value_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
