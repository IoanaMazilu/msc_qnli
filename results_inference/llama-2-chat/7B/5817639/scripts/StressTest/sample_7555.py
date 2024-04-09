entire_house_premise = 1
entire_house_hypothesis = 6

# the hypothesis talks about the time it takes Jim to clean the entire house, referenced also in the premise
if entire_house_hypothesis <= entire_house_premise:
    # check if the hypothesis value contradicts the estimate of more than 'entire_house_premise' hours
    label = "contradiction"
else:
    # the premise gives only an estimate for the time it takes Jim to clean the entire house
    # any time greater than 'entire_house_premise' hours is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
