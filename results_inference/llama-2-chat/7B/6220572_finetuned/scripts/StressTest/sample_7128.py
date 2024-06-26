# the hypothesis refers to the fraction of a sum of money T, referenced also in the premise
if 4/12 >= 7/12:
    # check if the fraction in the hypothesis contradicts the fraction in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the fraction
    # any fraction greater than '7/12' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
