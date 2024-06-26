arun_age = 25
deepak_age = 30

# the hypothesis talks about the ratio between the ages of Arun and Deepak
if arun_age / deepak_age <= 1 / 4:
    # check if the estimate of 'arun_age / deepak_age' contradicts the ratio mentioned in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio between the ages of Arun and Deepak
    # any ratio greater than 'arun_age / deepak_age' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
