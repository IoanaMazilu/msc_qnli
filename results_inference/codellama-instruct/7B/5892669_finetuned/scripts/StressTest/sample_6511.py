xyz_premise = 5
xyz_hypothesis = 7

# the hypothesis talks about the product of X, Y and Z, referenced also in the premise
if xyz_hypothesis <= xyz_premise:
    # check if the hypothesis value contradicts the estimate of more than 'xyz_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the product of X, Y and Z
    # any product greater than 'xyz_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
