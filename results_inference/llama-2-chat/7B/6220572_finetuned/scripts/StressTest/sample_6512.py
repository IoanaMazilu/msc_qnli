# the hypothesis talks about the product of X, Y and Z, referenced also in the premise
if 7!= 3:
    # check if the product of 7 in the hypothesis contradicts the product of 3 reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the product of X, Y and Z
    # any product of X, Y and Z consistent with the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
