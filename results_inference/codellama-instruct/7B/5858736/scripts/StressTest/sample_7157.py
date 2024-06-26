sandy_age = 4
molly_age = 3

# the hypothesis talks about the ratio between the ages of Sandy and Molly, referenced also in the premise
if sandy_age / molly_age <= 4/3:
    # check if the hypothesis value contradicts the estimate of more than '4/3'
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio between the ages of Sandy and Molly
    # any ratio greater than '4/3' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
