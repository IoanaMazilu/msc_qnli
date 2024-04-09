house_cleaning_premise = 6
house_cleaning_hypothesis = 5

# the hypothesis talks about the time it takes Jim to clean the entire house, which is also mentioned in the premise
if house_cleaning_hypothesis <= house_cleaning_premise:
    # check if the hypothesis value contradicts the estimate of 'house_cleaning_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time it takes Jim to clean the entire house
    # any time less than 'house_cleaning_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
