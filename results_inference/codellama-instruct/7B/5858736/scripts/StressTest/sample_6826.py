arun_age = 30
deepak_age = 35

# the hypothesis talks about the ratio between the ages of Arun and Deepak
if arun_age / deepak_age <= 3 / 3:
    # check if the hypothesis value contradicts the estimate of more than '3:3'
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio between the ages of Arun and Deepak
    # any ratio greater than '4:3' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
