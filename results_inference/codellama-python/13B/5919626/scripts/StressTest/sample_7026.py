minutes_cara = 120
minutes_dan = 520

# the hypothesis talks about the time difference between Dan and Cara
if minutes_dan <= minutes_cara:
    # check if the hypothesis value contradicts the estimate of more than'minutes_cara'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time difference between Dan and Cara
    # any time difference greater than'minutes_cara' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
