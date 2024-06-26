# the hypothesis talks about the number of boys in a school, referenced also in the premise
if 20 <= 80:
    # check if the hypothesis value contradicts the estimate of more than '80'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of boys
    # any number of boys greater than '80' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
