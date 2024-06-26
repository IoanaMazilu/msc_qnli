lewis_age = 25
brown_age = 50

# the hypothesis talks about the ratio of the ages of Lewis and Brown
if lewis_age / brown_age < 1:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio of the ages
    # any ratio greater than 1:2 is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
