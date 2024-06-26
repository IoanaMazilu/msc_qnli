# the hypothesis gives a specific number for Deepak's share, referenced also in the premise
if 1300 >= 4300:
    # check if the hypothesis value contradicts the estimate of less than '4300'
    label = "contradiction"
else:
    # the premise gives only an estimate for Deepak's share
    # any number of Deepak's share less than '4300' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
