xy_z_premise = 5
xy_z_hypothesis = 7

# the hypothesis talks about the product of X, Y and Z, referenced also in the premise
if xy_z_hypothesis <= xy_z_premise:
    # check if the hypothesis value contradicts the estimate of more than 'xy_z_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the product of X, Y and Z
    # any product greater than 'xy_z_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
