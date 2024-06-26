# define variables for premise and hypothesis
xy_z_premise = 7
xy_z_hypothesis = 5

# check if the hypothesis value contradicts the estimate of 'xy_z_premise'
if xy_z_hypothesis <= xy_z_premise:
    label = "contradiction"
else:
    # the premise gives only an estimate for the product of X, Y, and Z
    # any product of X, Y, and Z greater than 'xy_z_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
