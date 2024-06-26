outfit_premise = 3
outfit_hypothesis = 6

# the hypothesis talks about the number of outfits Jordan has, referenced also in the premise
if outfit_hypothesis <= outfit_premise:
    # check if the hypothesis value contradicts the estimate of 'outfit_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of outfits
    # any number of outfits greater than 'outfit_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
