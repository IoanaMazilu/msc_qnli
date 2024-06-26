arun_age = 4
deepak_age = 3

# the hypothesis talks about the ratio between the ages of Arun and Deepak
if arun_age / deepak_age!= 1/3:
    # check if the hypothesis value contradicts the ratio between the ages of Arun and Deepak mentioned in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio between the ages of Arun and Deepak
    # any ratio greater than 1:3 is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
