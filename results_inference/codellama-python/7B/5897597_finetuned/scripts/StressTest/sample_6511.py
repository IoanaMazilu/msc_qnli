XYZ_premise = 5
XYZ_hypothesis = 7

# the hypothesis refers to the possible product of X, Y and Z, which is also mentioned in the premise
if XYZ_hypothesis <= XYZ_premise:
    # check if the hypothesis value contradicts the estimate of more than 'XYZ_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the possible product of X, Y and Z
    # any product greater than 'XYZ_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
