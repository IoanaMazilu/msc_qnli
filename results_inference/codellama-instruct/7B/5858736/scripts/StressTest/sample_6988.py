anil_age = 70
son_age = 30

# the hypothesis talks about the ratio of the ages of Anil and his son at present
if anil_age / son_age <= 2 / 3:
    # check if the hypothesis value contradicts the estimate of more than '2:3'
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio of the ages of Anil and his son
    # any ratio greater than '2:3' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
