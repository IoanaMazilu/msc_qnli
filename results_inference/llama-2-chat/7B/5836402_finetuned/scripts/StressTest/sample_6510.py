XYZ_premise = 7
XYZ_hypothesis = 5

# the hypothesis talks about the possible product of X, Y, and Z, which are also referenced in the premise
if XYZ_hypothesis <= XYZ_premise:
    # check if the hypothesis value contradicts the estimate of more than 'XYZ_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the possible product
    # any product of X, Y, and Z greater than 'XYZ_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
