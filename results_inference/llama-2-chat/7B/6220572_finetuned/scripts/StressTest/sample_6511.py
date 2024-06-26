# the hypothesis refers to the product of X, Y and Z, mentioned also in the premise
if 7*XYZ_premise!= XYZ_hypothesis:
    # check if the product of X, Y and Z in the hypothesis contradicts the product in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the product of X, Y and Z
    # any product of X, Y and Z consistent with the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
